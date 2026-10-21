import { useCallback, useEffect, useState } from "react";
import api from "../../api/api";
import DashboardLayout from "../../components/layout/DashboardLayout";

function formatDate(value) {
  if (!value) return "—";

  const date = new Date(value);
  return Number.isNaN(date.getTime())
    ? String(value)
    : date.toLocaleString();
}

function formatDuration(value) {
  if (value == null || !Number.isFinite(Number(value))) return "—";

  const milliseconds = Number(value);

  if (milliseconds < 1000) return `${milliseconds.toFixed(1)} ms`;
  if (milliseconds < 60000) return `${(milliseconds / 1000).toFixed(2)} sec`;

  return `${(milliseconds / 60000).toFixed(2)} min`;
}

function statusStyle(status) {
  const value = String(status ?? "").toLowerCase();

  if (["completed", "success", "succeeded"].includes(value)) {
    return "bg-green-100 text-green-700";
  }

  if (["failed", "failure", "error", "aborted"].includes(value)) {
    return "bg-red-100 text-red-700";
  }

  if (["running", "in_progress", "pending"].includes(value)) {
    return "bg-blue-100 text-blue-700";
  }

  return "bg-slate-100 text-slate-700";
}

function getRuns(data) {
  if (Array.isArray(data)) return data;
  if (Array.isArray(data?.items)) return data.items;
  if (Array.isArray(data?.runs)) return data.runs;
  if (Array.isArray(data?.results)) return data.results;

  return [];
}

function getErrorMessage(error, fallback) {
  const detail = error.response?.data?.detail;

  if (typeof detail === "string") return detail;

  if (Array.isArray(detail)) {
    return detail
      .map((item) => item.msg ?? JSON.stringify(item))
      .join("; ");
  }

  if (!error.response) {
    return "Cannot connect to the backend. Make sure FastAPI is running.";
  }

  return fallback;
}

function ExecutionHistory() {
  const [runs, setRuns] = useState([]);
  const [selectedRun, setSelectedRun] = useState(null);
  const [loading, setLoading] = useState(true);
  const [detailLoading, setDetailLoading] = useState(false);
  const [error, setError] = useState("");
  const [detailError, setDetailError] = useState("");

  const fetchRuns = useCallback(async () => {
    setLoading(true);
    setError("");
    setDetailError("");

    try {
      const response = await api.get("/execution-history/");
      setRuns(getRuns(response.data));
    } catch (err) {
      setError(
        getErrorMessage(
          err,
          "Could not load execution history. Check your login and backend."
        )
      );
      setRuns([]);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchRuns();
  }, [fetchRuns]);

  const openRun = async (run) => {
    const runId = run.run_id ?? run.id;

    if (runId == null) {
      setDetailError("This workflow run does not contain a run ID.");
      return;
    }

    setSelectedRun(null);
    setDetailLoading(true);
    setDetailError("");

    try {
      const response = await api.get(`/execution-history/${runId}`);
      const data = response.data;

      const runData = data.run ?? data.workflow_run ?? data;
      const agentExecutions =
        data.agent_executions ?? data.executions ?? data.agents ?? [];

      setSelectedRun({
        ...run,
        ...runData,
        agent_executions: Array.isArray(agentExecutions)
          ? agentExecutions
          : [],
      });
    } catch (err) {
      setDetailError(
        getErrorMessage(err, `Could not load workflow run ${runId}.`)
      );
    } finally {
      setDetailLoading(false);
    }
  };

  const agentExecutions = selectedRun?.agent_executions ?? [];

  const completedRuns = runs.filter((run) => {
    const status = String(run.status ?? "").toLowerCase();

    return (
      ["completed", "success", "succeeded"].includes(status) ||
      run.success === true
    );
  }).length;

  const failedRuns = runs.filter((run) => {
    const status = String(run.status ?? "").toLowerCase();

    return (
      ["failed", "failure", "error", "aborted"].includes(status) ||
      run.success === false
    );
  }).length;

  return (
    <DashboardLayout>
      <div className="mx-auto max-w-7xl">
        <header className="mb-8 flex flex-col justify-between gap-4 sm:flex-row sm:items-center">
          <div>
            <p className="text-sm font-semibold uppercase tracking-wider text-blue-600">
              ECHO · Multi-Agent System
            </p>

            <h1 className="mt-2 text-3xl font-bold text-slate-900">
              📊 Execution History
            </h1>

            <p className="mt-2 text-slate-600">
              Inspect workflow runs, execution times, and individual agent results.
            </p>
          </div>

          <button
            type="button"
            onClick={fetchRuns}
            disabled={loading}
            className="rounded-lg bg-blue-600 px-5 py-3 font-medium text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Refreshing..." : "Refresh history"}
          </button>
        </header>

        {error && (
          <div
            role="alert"
            className="mb-6 rounded-xl border border-red-200 bg-red-50 p-4 text-red-700"
          >
            {error}
          </div>
        )}

        {detailError && (
          <div
            role="alert"
            className="mb-6 rounded-xl border border-red-200 bg-red-50 p-4 text-red-700"
          >
            {detailError}
          </div>
        )}

        <section className="mb-8 grid grid-cols-1 gap-4 sm:grid-cols-3">
          <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
            <p className="text-sm text-slate-500">Total runs loaded</p>
            <p className="mt-2 text-3xl font-bold text-slate-900">
              {runs.length}
            </p>
          </div>

          <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
            <p className="text-sm text-slate-500">Completed runs</p>
            <p className="mt-2 text-3xl font-bold text-green-600">
              {completedRuns}
            </p>
          </div>

          <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
            <p className="text-sm text-slate-500">Failed runs</p>
            <p className="mt-2 text-3xl font-bold text-red-600">
              {failedRuns}
            </p>
          </div>
        </section>

        <section className="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
          <div className="border-b border-slate-200 px-5 py-4">
            <h2 className="text-lg font-semibold text-slate-900">
              Workflow runs
            </h2>
          </div>

          {loading ? (
            <div className="p-10 text-center text-slate-500">
              Loading execution history...
            </div>
          ) : runs.length === 0 ? (
            <div className="p-10 text-center">
              <p className="font-medium text-slate-700">
                No workflow runs found.
              </p>
              <p className="mt-2 text-sm text-slate-500">
                Run a workflow in ECHO, then refresh this page.
              </p>
            </div>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full min-w-[760px] text-left text-sm">
                <thead className="bg-slate-50 text-slate-500">
                  <tr>
                    <th className="px-5 py-4 font-medium">Run ID</th>
                    <th className="px-5 py-4 font-medium">Workflow</th>
                    <th className="px-5 py-4 font-medium">Status</th>
                    <th className="px-5 py-4 font-medium">Duration</th>
                    <th className="px-5 py-4 font-medium">Started</th>
                    <th className="px-5 py-4 font-medium">Action</th>
                  </tr>
                </thead>

                <tbody className="divide-y divide-slate-100">
                  {runs.map((run, index) => {
                    const runId = run.run_id ?? run.id ?? index;
                    const status =
                      run.status ?? (run.success ? "completed" : "unknown");

                    return (
                      <tr key={runId} className="hover:bg-slate-50">
                        <td className="px-5 py-4 font-semibold text-slate-800">
                          #{runId}
                        </td>
                        <td className="px-5 py-4 text-slate-700">
                          {run.workflow_name ?? run.workflow ?? "Workflow"}
                        </td>
                        <td className="px-5 py-4">
                          <span
                            className={`inline-flex rounded-full px-3 py-1 text-xs font-semibold ${statusStyle(status)}`}
                          >
                            {status}
                          </span>
                        </td>
                        <td className="px-5 py-4 text-slate-600">
                          {formatDuration(run.total_duration_ms)}
                        </td>
                        <td className="px-5 py-4 text-slate-600">
                          {formatDate(run.started_at)}
                        </td>
                        <td className="px-5 py-4">
                          <button
                            type="button"
                            onClick={() => openRun(run)}
                            className="font-semibold text-blue-600 hover:text-blue-800"
                          >
                            View details →
                          </button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          )}
        </section>

        {(detailLoading || selectedRun) && (
          <section className="mt-8 rounded-xl border border-slate-200 bg-white p-5 shadow-sm sm:p-6">
            {detailLoading ? (
              <p className="py-8 text-center text-slate-500">
                Loading workflow details...
              </p>
            ) : (
              <>
                <div className="mb-6 flex flex-col justify-between gap-3 sm:flex-row sm:items-start">
                  <div>
                    <h2 className="text-xl font-bold text-slate-900">
                      Workflow run #{selectedRun.run_id ?? selectedRun.id}
                    </h2>
                    <p className="mt-1 text-sm text-slate-500">
                      {selectedRun.workflow_name ??
                        selectedRun.workflow ??
                        "Workflow"}
                    </p>
                  </div>

                  <button
                    type="button"
                    onClick={() => {
                      setSelectedRun(null);
                      setDetailError("");
                    }}
                    className="self-start rounded-lg border border-slate-200 px-4 py-2 text-sm font-medium text-slate-600 hover:bg-slate-50"
                  >
                    Close details
                  </button>
                </div>

                <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
                  <div className="rounded-lg bg-slate-50 p-4">
                    <p className="text-sm text-slate-500">Status</p>
                    <p className="mt-2 font-semibold text-slate-900">
                      {selectedRun.status ?? "—"}
                    </p>
                  </div>

                  <div className="rounded-lg bg-slate-50 p-4">
                    <p className="text-sm text-slate-500">Total duration</p>
                    <p className="mt-2 font-semibold text-slate-900">
                      {formatDuration(selectedRun.total_duration_ms)}
                    </p>
                  </div>

                  <div className="rounded-lg bg-slate-50 p-4">
                    <p className="text-sm text-slate-500">
                      Agent execution time
                    </p>
                    <p className="mt-2 font-semibold text-slate-900">
                      {formatDuration(
                        selectedRun.agent_execution_duration_ms
                      )}
                    </p>
                  </div>

                  <div className="rounded-lg bg-slate-50 p-4">
                    <p className="text-sm text-slate-500">Finished</p>
                    <p className="mt-2 text-sm font-semibold text-slate-900">
                      {formatDate(selectedRun.finished_at)}
                    </p>
                  </div>
                </div>

                {selectedRun.abort_reason && (
                  <div className="mb-6 rounded-lg border border-amber-200 bg-amber-50 p-4 text-sm text-amber-800">
                    <strong>Abort reason:</strong>{" "}
                    {selectedRun.abort_reason}
                  </div>
                )}

                <h3 className="mb-4 text-lg font-semibold text-slate-900">
                  Agent executions
                </h3>

                {agentExecutions.length === 0 ? (
                  <p className="rounded-lg bg-slate-50 p-5 text-sm text-slate-500">
                    No individual agent execution records were returned for this run.
                  </p>
                ) : (
                  <div className="space-y-3">
                    {agentExecutions.map((agent, index) => (
                      <div
                        key={agent.id ?? agent.agent_name ?? index}
                        className="rounded-lg border border-slate-200 p-4"
                      >
                        <div className="flex flex-col justify-between gap-3 sm:flex-row sm:items-center">
                          <div>
                            <p className="font-semibold text-slate-900">
                              {agent.agent_name ??
                                agent.agent ??
                                agent.name ??
                                `Agent ${index + 1}`}
                            </p>
                            <p className="mt-1 text-sm text-slate-500">
                              Duration:{" "}
                              {formatDuration(
                                agent.duration_ms ??
                                  agent.execution_duration_ms
                              )}
                            </p>
                          </div>

                          <span
                            className={`self-start rounded-full px-3 py-1 text-xs font-semibold ${statusStyle(agent.status)}`}
                          >
                            {agent.status ?? "unknown"}
                          </span>
                        </div>

                        {agent.error_summary && (
                          <p className="mt-3 rounded-md bg-red-50 p-3 text-sm text-red-700">
                            {agent.error_summary}
                          </p>
                        )}
                      </div>
                    ))}
                  </div>
                )}
              </>
            )}
          </section>
        )}
      </div>
    </DashboardLayout>
  );
}

export default ExecutionHistory;