from langchain.agents import Tool
from input_agent import extract_cobol_from_docx
from semantic_agent import convert_to_structured_format
from rule_extractor_agent import extract_business_rules
from validator_agent import validate_rules
from output_agent import write_rules_to_docx

extract_cobol_tool = Tool(
    name="ExtractCOBOL",
    func=extract_cobol_from_docx,
    description="Extracts COBOL code from a DOCX file."
)

semantic_tool = Tool(
    name="SemanticConverter",
    func=convert_to_structured_format,
    description="Converts COBOL logic into structured format."
)

rule_extractor_tool = Tool(
    name="BusinessRuleExtractor",
    func=extract_business_rules,
    description="Extracts business rules from structured COBOL logic."
)

validator_tool = Tool(
    name="RuleValidator",
    func=validate_rules,
    description="Validates business rules."
)

docx_writer_tool = Tool(
    name="DOCXWriter",
    func=write_rules_to_docx,
    description="Writes validated business rules to a DOCX file."
)

all_tools = [
    extract_cobol_tool,
    semantic_tool,
    rule_extractor_tool,
    validator_tool,
    docx_writer_tool
]
