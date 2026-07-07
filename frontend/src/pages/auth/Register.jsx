import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../api/api";

export default function Register() {
    const navigate = useNavigate();

    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    async function handleRegister(e) {
        e.preventDefault();

        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            return;
        }

        try {

            await api.post("/auth/register", {
                full_name:name,
                email,
                password,
            });

            alert("Account created successfully!");

            navigate("/login");

        } catch (err) {

            console.error(err);

            alert("Registration failed.");

        }
    }

    return (
        <div className="flex justify-center items-center min-h-screen bg-slate-100">

            <form
                onSubmit={handleRegister}
                className="bg-white shadow-xl rounded-xl p-8 w-96"
            >

                <h1 className="text-3xl font-bold text-center mb-6">
                    Create Account
                </h1>

                <input
                    className="border w-full p-3 rounded mb-4"
                    placeholder="Full Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />

                <input
                    className="border w-full p-3 rounded mb-4"
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                <input
                    className="border w-full p-3 rounded mb-4"
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <input
                    className="border w-full p-3 rounded mb-6"
                    type="password"
                    placeholder="Confirm Password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                />

                <button
                    className="bg-green-600 hover:bg-green-700 text-white w-full p-3 rounded"
                >
                    Create Account
                </button>

                <div className="mt-6 text-center">
                    <p className="text-gray-600">
                        Already have an account?{" "}
                        <button
                            type="button"
                            onClick={() => navigate("/login")}
                            className="text-blue-600 font-semibold hover:underline"
                        >
                            Login
                        </button>
                    </p>
                </div>

            </form>

        </div>
    );
}