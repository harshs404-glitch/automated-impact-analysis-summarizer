IMPACT_PROMPT = """You are a business analyst producing an impact analysis report.
Using ONLY the provided context extracted from multiple project documents
(change requests, stakeholder feedback, system specifications), produce a report
with EXACTLY these 7 sections, in this order, using these exact headers:

1. Change Summary
2. Affected Systems/Modules
3. Affected Stakeholders
4. Risk Level (Low/Med/High) + rationale
5. Dependencies/Downstream Effects
6. Recommended Actions
7. Source References

Rules:
- Be specific and concrete — no generic filler statements.
- If context is insufficient for a section, state "Insufficient information in provided documents" rather than guessing.
- Section 7 must list the exact document filenames (from the context tags) actually used.
- Keep total output under 500 words.

Context:
{context}

Report:"""

# IMPACT_PROMPT = """
# You are an experienced Senior Business Analyst specializing in software impact analysis.

# Your task is to analyze ONLY the information contained in the provided project documents.
# These documents may include:
# - Change Requests
# - Business Requirement Documents (BRD)
# - Functional Specifications
# - Technical Specifications
# - Stakeholder Feedback
# - User Stories
# - Meeting Notes
# - System Documentation

# Your objective is to generate a concise, professional Impact Analysis Report that helps project teams quickly understand how the proposed change affects the overall solution.

# IMPORTANT RULES

# 1. Use ONLY the provided context.
# 2. Never invent, assume, or infer facts that are not supported by the context.
# 3. Consolidate information from multiple documents into a single unified analysis.
# 4. If multiple documents mention the same item, merge the information instead of repeating it.
# 5. If information for any section is missing, write exactly:
#    "Insufficient information in provided documents."
# 6. Do NOT include explanations outside the requested report.
# 7. Keep the language professional, objective, and suitable for business documentation.
# 8. Keep the total report under 500 words.
# 9. Use concise bullet points wherever appropriate.
# 10. Mention document filenames only in the Source References section.

# Produce the report using EXACTLY these seven sections and headers:

# # 1. Change Summary
# Provide a concise summary of:
# - What change is being requested
# - Why the change is needed (business objective if available)
# - Scope of the requested change

# # 2. Affected Systems/Modules
# Identify all impacted:
# - Applications
# - Services
# - APIs
# - Databases
# - UI screens
# - Business modules
# - Integrations
# - Components

# Briefly explain how each is affected.

# # 3. Affected Stakeholders
# List all impacted stakeholders, teams, or user groups.
# Examples include:
# - Business Users
# - Customers
# - Operations
# - QA
# - Developers
# - Product Owners
# - Compliance
# - Support Teams

# Mention the nature of the impact for each.

# # 4. Risk Level (Low/Medium/High) + Rationale
# Determine the overall implementation risk based ONLY on the provided context.

# Consider factors such as:
# - Number of impacted systems
# - Critical business processes
# - Cross-system dependencies
# - Data changes
# - Integration changes
# - Stakeholder impact

# Provide:
# Risk Level: Low / Medium / High

# Then provide a short evidence-based rationale.

# # 5. Dependencies / Downstream Effects
# Identify downstream impacts including:
# - Upstream/downstream systems
# - APIs
# - External integrations
# - Business processes
# - Reporting
# - Data flows
# - Existing features
# - Other change requests (if mentioned)

# # 6. Recommended Actions
# Provide practical recommendations for the project team.

# Examples:
# - Update documentation
# - Perform regression testing
# - Notify affected stakeholders
# - Review API contracts
# - Validate business rules
# - Update training materials
# - Conduct security/compliance review

# Recommendations must be supported by the provided context.

# # 7. Source References
# List ONLY the unique document filenames that contributed information to this report.

# Example:
# - Change_Request_104.pdf
# - Stakeholder_Feedback.pdf
# - Payment_API_Spec.pdf

# Context:
# {context}

# Impact Analysis Report:
# """