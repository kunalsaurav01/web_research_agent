# def synthesize_summary(analyzed_data):
#     print("🧬 [Mock Synthesizer] Generating summary...")
#     # Check for relevant keywords to synthesize a summary
#     if "healthcare" in analyzed_data.lower():
#         return [
#             "AI is revolutionizing healthcare with personalized diagnostics.",
#             "Telemedicine has brought healthcare to underserved areas.",
#             "Data privacy remains a concern in the healthcare industry."
#         ]
#     else:
#         return [
#             "This article discusses recent advancements in the field.",
#             "Experts predict a bright future with technology integration.",
#             "New innovations are expected to reshape industries."
#         ]

def synthesize_summary(contents):
    summaries = []
    for content in contents:
        if content:
            first_sentence = content.split('.')[0] + '.'
            summaries.append(first_sentence.strip())
        else:
            summaries.append("No content available.")

    return summaries
