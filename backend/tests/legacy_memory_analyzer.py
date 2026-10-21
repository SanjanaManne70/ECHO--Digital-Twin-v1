from app.ai.memory_analyzer import MemoryAnalyzer

analyzer = MemoryAnalyzer()

result = analyzer.analyze(
    title="Failed Coding Interview",
    description="I studied for months but couldn't solve the coding questions.",
    domain="Career",
)

print("\n====== FINAL ANALYSIS ======")
print(result)
print("============================")