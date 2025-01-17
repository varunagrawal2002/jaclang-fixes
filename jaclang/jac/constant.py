"""Constants across the project."""
from enum import Enum, auto


class Constants(str, Enum):
    """Token constants for Jac."""

    JAC_LANG_IMP = "jac"
    JAC_DEBUG_SPLITTER = "JAC DEBUG INFO"
    PATCH = "PATCH"

    JAC_TMP = "_jac_tmp"
    EXEC_CONTEXT = "_jac_exec_ctx_"
    HERE = "_jac_here_"
    ROOT = f"{EXEC_CONTEXT}.get_root()"
    EDGES_TO_NODE = "_jac_edges_to_nodes_"
    EDGE_REF = "_jac_edge_ref_"
    CONNECT_NODE = "_jac_connect_node_"
    DISCONNECT_NODE = "_jac_disconnect_node_"
    WALKER_VISIT = "_jac_visit_"
    DISENGAGE = "_jac_disengage_"
    OBJECT_CLASS = "_jac_Object_"
    NODE_CLASS = "_jac_Node_"
    EDGE_CLASS = "_jac_Edge_"
    WALKER_CLASS = "_jac_Walker_"
    WITH_DIR = "_jac_apply_dir_"
    EDGE_DIR = "_jac_Edge_Dir_"

    def __str__(self) -> str:
        """Return the string representation of the token."""
        return self.value


class EdgeDir(Enum):
    """Edge direction indicator."""

    IN = auto()
    OUT = auto()
    ANY = auto()


class Values(int, Enum):
    """Token constants for Jac."""

    JAC_ERROR_LINE_RANGE = 3


# Done like this for type checker
# validated synced with test
class Tokens(str, Enum):
    """Token constants for the lexer."""

    FLOAT = "FLOAT"
    STRING = "STRING"
    DOC_STRING = "DOC_STRING"
    FSTRING = "FSTRING"
    BOOL = "BOOL"
    INT = "INT"
    HEX = "HEX"
    BIN = "BIN"
    OCT = "OCT"
    NULL = "NULL"
    NAME = "NAME"
    KWESC_NAME = "KWESC_NAME"
    TYP_STRING = "TYP_STRING"
    TYP_INT = "TYP_INT"
    TYP_FLOAT = "TYP_FLOAT"
    TYP_LIST = "TYP_LIST"
    TYP_TUPLE = "TYP_TUPLE"
    TYP_SET = "TYP_SET"
    TYP_DICT = "TYP_DICT"
    TYP_BOOL = "TYP_BOOL"
    TYP_BYTES = "TYP_BYTES"
    TYP_ANY = "TYP_ANY"
    TYP_TYPE = "TYP_TYPE"
    KW_FREEZE = "KW_FREEZE"
    KW_OBJECT = "KW_OBJECT"
    KW_ENUM = "KW_ENUM"
    KW_NODE = "KW_NODE"
    KW_IGNORE = "KW_IGNORE"
    KW_VISIT = "KW_VISIT"
    KW_REVISIT = "KW_REVISIT"
    KW_SPAWN = "KW_SPAWN"
    KW_WITH = "KW_WITH"
    KW_ENTRY = "KW_ENTRY"
    KW_EXIT = "KW_EXIT"
    KW_IMPORT = "KW_IMPORT"
    KW_INCLUDE = "KW_INCLUDE"
    KW_FROM = "KW_FROM"
    KW_AS = "KW_AS"
    KW_EDGE = "KW_EDGE"
    KW_WALKER = "KW_WALKER"
    KW_ASYNC = "KW_ASYNC"
    KW_AWAIT = "KW_AWAIT"
    KW_TEST = "KW_TEST"
    KW_ASSERT = "KW_ASSERT"
    COLON = "COLON"
    PIPE_FWD = "PIPE_FWD"
    PIPE_BKWD = "PIPE_BKWD"
    DOT_FWD = "DOT_FWD"
    DOT_BKWD = "DOT_BKWD"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    SEMI = "SEMI"
    EQ = "EQ"
    ADD_EQ = "ADD_EQ"
    SUB_EQ = "SUB_EQ"
    MUL_EQ = "MUL_EQ"
    FLOOR_DIV_EQ = "FLOOR_DIV_EQ"
    DIV_EQ = "DIV_EQ"
    MOD_EQ = "MOD_EQ"
    BW_AND_EQ = "BW_AND_EQ"
    BW_OR_EQ = "BW_OR_EQ"
    BW_XOR_EQ = "BW_XOR_EQ"
    BW_NOT_EQ = "BW_NOT_EQ"
    LSHIFT_EQ = "LSHIFT_EQ"
    RSHIFT_EQ = "RSHIFT_EQ"
    WALRUS_EQ = "WALRUS_EQ"
    KW_AND = "KW_AND"
    KW_OR = "KW_OR"
    KW_IF = "KW_IF"
    KW_ELIF = "KW_ELIF"
    KW_ELSE = "KW_ELSE"
    KW_FOR = "KW_FOR"
    KW_TO = "KW_TO"
    KW_BY = "KW_BY"
    KW_WHILE = "KW_WHILE"
    KW_CONTINUE = "KW_CONTINUE"
    KW_BREAK = "KW_BREAK"
    KW_DISENGAGE = "KW_DISENGAGE"
    KW_YIELD = "KW_YIELD"
    KW_SKIP = "KW_SKIP"
    KW_REPORT = "KW_REPORT"
    KW_RETURN = "KW_RETURN"
    KW_DELETE = "KW_DELETE"
    KW_TRY = "KW_TRY"
    KW_EXCEPT = "KW_EXCEPT"
    KW_FINALLY = "KW_FINALLY"
    KW_RAISE = "KW_RAISE"
    DOT = "DOT"
    NOT = "NOT"
    EE = "EE"
    LT = "LT"
    GT = "GT"
    LTE = "LTE"
    GTE = "GTE"
    NE = "NE"
    KW_IN = "KW_IN"
    KW_IS = "KW_IS"
    KW_NIN = "KW_NIN"
    KW_ISN = "KW_ISN"
    KW_PRIV = "KW_PRIV"
    KW_PUB = "KW_PUB"
    KW_PROT = "KW_PROT"
    KW_HAS = "KW_HAS"
    KW_GLOBAL = "KW_GLOBAL"
    COMMA = "COMMA"
    KW_CAN = "KW_CAN"
    KW_STATIC = "KW_STATIC"
    PLUS = "PLUS"
    MINUS = "MINUS"
    STAR_MUL = "STAR_MUL"
    FLOOR_DIV = "FLOOR_DIV"
    DIV = "DIV"
    MOD = "MOD"
    BW_AND = "BW_AND"
    BW_OR = "BW_OR"
    BW_XOR = "BW_XOR"
    BW_NOT = "BW_NOT"
    LSHIFT = "LSHIFT"
    RSHIFT = "RSHIFT"
    STAR_POW = "STAR_POW"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LSQUARE = "LSQUARE"
    RSQUARE = "RSQUARE"
    ARROW_L = "ARROW_L"
    ARROW_R = "ARROW_R"
    ARROW_BI = "ARROW_BI"
    ARROW_L_p1 = "ARROW_L_p1"
    ARROW_L_p2 = "ARROW_L_p2"
    ARROW_R_p1 = "ARROW_R_p1"
    ARROW_R_p2 = "ARROW_R_p2"
    CARROW_L = "CARROW_L"
    CARROW_R = "CARROW_R"
    CARROW_L_p1 = "CARROW_L_p1"
    CARROW_L_p2 = "CARROW_L_p2"
    CARROW_R_p1 = "CARROW_R_p1"
    CARROW_R_p2 = "CARROW_R_p2"
    GLOBAL_OP = "GLOBAL_OP"
    HERE_OP = "HERE_OP"
    SELF_OP = "SELF_OP"
    INIT_OP = "INIT_OP"
    SUPER_OP = "SUPER_OP"
    ROOT_OP = "ROOT_OP"
    WALKER_OP = "WALKER_OP"
    NODE_OP = "NODE_OP"
    EDGE_OP = "EDGE_OP"
    OBJECT_OP = "OBJECT_OP"
    ENUM_OP = "ENUM_OP"
    ABILITY_OP = "ABILITY_OP"
    A_PIPE_FWD = "A_PIPE_FWD"
    A_PIPE_BKWD = "A_PIPE_BKWD"
    ELVIS_OP = "ELVIS_OP"
    RETURN_HINT = "RETURN_HINT"
    NULL_OK = "NULL_OK"
    DECOR_OP = "DECOR_OP"

    def __str__(self) -> str:
        """Return the string representation of the token."""
        return self.value
