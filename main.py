def generate_report(stats, contamination):
    print("\n📊 FINAL REPORT")
    print("--------------------")

    total_sequences = stats.get("total_sequences", 0)
    avg_length = stats.get("avg_length", 0)
    contaminated = len(contamination)

    print(f"Total Sequences : {total_sequences}")
    print(f"Avg Length      : {avg_length}")
    print(f"Contaminated    : {contaminated}")

    return {
        "total_sequences": total_sequences,
        "avg_length": avg_length,
        "contaminated": contaminated
    }