TEXT = "text"
INTENT = "intent"
RESPONSE = "response"
INTENT_RESPONSE_KEY = "intent_response_key"
ACTION_TEXT = "action_text"
ACTION_NAME = "action_name"
INTENT_NAME = "intent_name"
METADATA = "metadata"
METADATA_INTENT = "intent"
METADATA_EXAMPLE = "example"

RESPONSE_IDENTIFIER_DELIMITER = "/"

FEATURE_TYPE_SENTENCE = "sentence"
FEATURE_TYPE_SEQUENCE = "sequence"
VALID_FEATURE_TYPES = [FEATURE_TYPE_SEQUENCE, FEATURE_TYPE_SENTENCE]

EXTRACTOR = "extractor"
PRETRAINED_EXTRACTORS = {"DucklingHTTPExtractor", "SpacyEntityExtractor"}
TRAINABLE_EXTRACTORS = {"MitieEntityExtractor", "CRFEntityExtractor", "DIETClassifier"}

ENTITIES = "entities"
ENTITY_ATTRIBUTE_TYPE = "entity"
ENTITY_ATTRIBUTE_GROUP = "group"
ENTITY_ATTRIBUTE_ROLE = "role"
ENTITY_ATTRIBUTE_VALUE = "value"
ENTITY_ATTRIBUTE_START = "start"
ENTITY_ATTRIBUTE_END = "end"
NO_ENTITY_TAG = "O"
