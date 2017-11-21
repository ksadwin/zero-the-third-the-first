# look at all these constants. Thanks github user moonshadow565!
# (repo Pyxiex3, LINK https://github.com/moonshadow565/Pyxiex3/blob/4d0e08727abcf9e4108f6c35e613f91f70ebd52f/Cpp/cah.h)

CAH_AjaxOperation_FIRST_LOAD = "fl"
CAH_AjaxOperation_START_GAME = "sg"
CAH_AjaxOperation_JUDGE_SELECT = "js"
CAH_AjaxOperation_LOG_OUT = "lo"
CAH_AjaxOperation_GAME_LIST = "ggl"
CAH_AjaxOperation_CHANGE_GAME_OPTIONS = "cgo"
CAH_AjaxOperation_PLAY_CARD = "pc"
CAH_AjaxOperation_CREATE_GAME = "cg"
CAH_AjaxOperation_CARDCAST_LIST_CARDSETS = "clc"
CAH_AjaxOperation_GAME_CHAT = "GC"
CAH_AjaxOperation_KICK = "K"
CAH_AjaxOperation_ADMIN_SET_VERBOSE_LOG = "svl"
CAH_AjaxOperation_GET_CARDS = "gc"
CAH_AjaxOperation_JOIN_GAME = "jg"
CAH_AjaxOperation_CHAT = "c"
CAH_AjaxOperation_NAMES = "gn"
CAH_AjaxOperation_SPECTATE_GAME = "vg"
CAH_AjaxOperation_BAN = "b"
CAH_AjaxOperation_SCORE = "SC"
CAH_AjaxOperation_GET_GAME_INFO = "ggi"
CAH_AjaxOperation_CARDCAST_ADD_CARDSET = "cac"
CAH_AjaxOperation_CARDCAST_REMOVE_CARDSET = "crc"
CAH_AjaxOperation_REGISTER = "r"
CAH_AjaxOperation_STOP_GAME = "Sg"
CAH_AjaxOperation_LEAVE_GAME = "lg"

CAH_AjaxRequest_WALL = "wall"
CAH_AjaxRequest_MESSAGE = "m"
CAH_AjaxRequest_CARD_ID = "cid"
CAH_AjaxRequest_GAME_ID = "gid"
CAH_AjaxRequest_EMOTE = "me"
CAH_AjaxRequest_CARDCAST_ID = "cci"
CAH_AjaxRequest_GAME_OPTIONS = "go"
CAH_AjaxRequest_SERIAL = "s"
CAH_AjaxRequest_PASSWORD = "pw"
CAH_AjaxRequest_OP = "o"
CAH_AjaxRequest_NICKNAME = "n"


CAH_AjaxResponse_WHITE_CARDS = "wc"
CAH_AjaxResponse_CARD_SETS = "css"
CAH_AjaxResponse_GAME_ID = "gid"
CAH_AjaxResponse_HAND = "h"
CAH_AjaxResponse_PLAYER_INFO = "pi"
CAH_AjaxResponse_BLACK_CARD = "bc"
CAH_AjaxResponse_GAME_OPTIONS = "go"
CAH_AjaxResponse_IN_PROGRESS = "ip"
CAH_AjaxResponse_GAMES = "gl"
CAH_AjaxResponse_NICKNAME = "n"
CAH_AjaxResponse_CARD_ID = "cid"
CAH_AjaxResponse_NEXT = "next"
CAH_AjaxResponse_GAME_INFO = "gi"
CAH_AjaxResponse_ERROR = "e"
CAH_AjaxResponse_ERROR_CODE = "ec"
CAH_AjaxResponse_SERIAL = "s"
CAH_AjaxResponse_MAX_GAMES = "mg"
CAH_AjaxResponse_NAMES = "nl"


CAH_BlackCardData_TEXT = "T"
CAH_BlackCardData_PICK = "PK"
CAH_BlackCardData_ID = "cid"
CAH_BlackCardData_WATERMARK = "W"
CAH_BlackCardData_DRAW = "D"


CAH_CardSetData_CARD_SET_DESCRIPTION = "csd"
CAH_CardSetData_WEIGHT = "w"
CAH_CardSetData_CARD_SET_NAME = "csn"
CAH_CardSetData_ID = "cid"
CAH_CardSetData_WHITE_CARDS_IN_DECK = "wcid"
CAH_CardSetData_BLACK_CARDS_IN_DECK = "bcid"
CAH_CardSetData_BASE_DECK = "bd"


CAH_DisconnectReason_BANNED = "B&"
CAH_DisconnectReason_PING_TIMEOUT = "pt"
CAH_DisconnectReason_KICKED = "k"
CAH_DisconnectReason_MANUAL = "man"
CAH_DisconnectReason_IDLE_TIMEOUT = "it"


CAH_ErrorCode_TOO_MANY_GAMES = "tmg"
CAH_ErrorCode_NO_CARD_SPECIFIED = "ncs"
CAH_ErrorCode_ACCESS_DENIED = "ad"
CAH_ErrorCode_NOT_GAME_HOST = "ngh"
CAH_ErrorCode_CANNOT_JOIN_ANOTHER_GAME = "cjag"
CAH_ErrorCode_INVALID_CARD = "ic"
CAH_ErrorCode_RESERVED_NICK = "rn"
CAH_ErrorCode_TOO_MANY_USERS = "tmu"
CAH_ErrorCode_NO_GAME_SPECIFIED = "ngs"
CAH_ErrorCode_SESSION_EXPIRED = "se"
CAH_ErrorCode_CARDCAST_INVALID_ID = "cii"
CAH_ErrorCode_BAD_OP = "bo"
CAH_ErrorCode_TOO_FAST = "tf"
CAH_ErrorCode_NO_SESSION = "ns"
CAH_ErrorCode_NOT_REGISTERED = "nr"
CAH_ErrorCode_OP_NOT_SPECIFIED = "ons"
CAH_ErrorCode_NOT_JUDGE = "nj"
CAH_ErrorCode_WRONG_PASSWORD = "wp"
CAH_ErrorCode_NOT_IN_THAT_GAME = "nitg"
CAH_ErrorCode_NICK_IN_USE = "niu"
CAH_ErrorCode_SERVER_ERROR = "serr"
CAH_ErrorCode_GAME_FULL = "gf"
CAH_ErrorCode_NO_NICK_SPECIFIED = "nns"
CAH_ErrorCode_NOT_ADMIN = "na"
CAH_ErrorCode_NOT_YOUR_TURN = "nyt"
CAH_ErrorCode_BANNED = "B&"
CAH_ErrorCode_INVALID_NICK = "in"
CAH_ErrorCode_ALREADY_STARTED = "as"
CAH_ErrorCode_BAD_REQUEST = "br"
CAH_ErrorCode_NO_SUCH_USER = "nsu"
CAH_ErrorCode_DO_NOT_HAVE_CARD = "dnhc"
CAH_ErrorCode_MESSAGE_TOO_LONG = "mtl"
CAH_ErrorCode_ALREADY_STOPPED = "aS"
CAH_ErrorCode_NOT_ENOUGH_PLAYERS = "nep"
CAH_ErrorCode_INVALID_GAME = "ig"
CAH_ErrorCode_CARDCAST_CANNOT_FIND = "ccf"
CAH_ErrorCode_NO_MSG_SPECIFIED = "nms"
CAH_ErrorCode_NOT_ENOUGH_CARDS = "nec"


CAH_GameInfo_HOST = "H"
CAH_GameInfo_STATE = "S"
CAH_GameInfo_PLAYERS = "P"
CAH_GameInfo_SPECTATORS = "V"
CAH_GameInfo_ID = "gid"
CAH_GameInfo_GAME_OPTIONS = "go"
CAH_GameInfo_HAS_PASSWORD = "hp"



CAH_GameOptionData_TIMER_MULTIPLIER =  "ut"
CAH_GameOptionData_CARD_SETS = "css"
CAH_GameOptionData_BLANKS_LIMIT = "bl"
CAH_GameOptionData_SPECTATOR_LIMIT = "vL"
CAH_GameOptionData_PLAYER_LIMIT = "pL"
CAH_GameOptionData_PASSWORD = "pw"
CAH_GameOptionData_SCORE_LIMIT = "sl"


CAH_GamePlayerInfo_NAME = "N"
CAH_GamePlayerInfo_SCORE = "sc"
CAH_GamePlayerInfo_STATUS = "st"


CAH_GamePlayerStatus_SPECTATOR = "sv"
CAH_GamePlayerStatus_HOST = "sh"
CAH_GamePlayerStatus_IDLE = "si"
CAH_GamePlayerStatus_WINNER = "sw"
CAH_GamePlayerStatus_PLAYING = "sp"
CAH_GamePlayerStatus_JUDGE = "sj"
CAH_GamePlayerStatus_JUDGING = "sjj"


CAH_GameState_PLAYING = "p"
CAH_GameState_ROUND_OVER = "ro"
CAH_GameState_LOBBY = "l"
CAH_GameState_JUDGING = "j"
CAH_GameState_DEALING = "d"

CAH_LongPollEvent_KICKED = "k"
CAH_LongPollEvent_HURRY_UP = "hu"
CAH_LongPollEvent_GAME_JUDGE_SKIPPED = "gjs"
CAH_LongPollEvent_GAME_PLAYER_LEAVE = "gpl"
CAH_LongPollEvent_KICKED_FROM_GAME_IDLE = "kfgi"
CAH_LongPollEvent_GAME_ROUND_COMPLETE = "grc"
CAH_LongPollEvent_GAME_STATE_CHANGE = "gsc"
CAH_LongPollEvent_GAME_OPTIONS_CHANGED = "goc"
CAH_LongPollEvent_GAME_PLAYER_SKIPPED = "gps"
CAH_LongPollEvent_CHAT = "c"
CAH_LongPollEvent_BANNED = "B&"
CAH_LongPollEvent_GAME_SPECTATOR_LEAVE = "gvl"
CAH_LongPollEvent_CARDCAST_ADD_CARDSET = "cac"
CAH_LongPollEvent_NEW_PLAYER = "np"
CAH_LongPollEvent_GAME_PLAYER_JOIN = "gpj"
CAH_LongPollEvent_GAME_SPECTATOR_JOIN = "gvj"
CAH_LongPollEvent_GAME_LIST_REFRESH = "glr"
CAH_LongPollEvent_NOOP = "_"
CAH_LongPollEvent_GAME_PLAYER_KICKED_IDLE = "gpki"
CAH_LongPollEvent_GAME_PLAYER_INFO_CHANGE = "gpic"
CAH_LongPollEvent_CARDCAST_REMOVE_CARDSET = "crc"
CAH_LongPollEvent_GAME_BLACK_RESHUFFLE = "gbr"
CAH_LongPollEvent_GAME_WHITE_RESHUFFLE = "gwr"
CAH_LongPollEvent_PLAYER_LEAVE = "pl"
CAH_LongPollEvent_HAND_DEAL = "hd"
CAH_LongPollEvent_GAME_JUDGE_LEFT = "gjl"


CAH_LongPollResponse_WALL = "wall"
CAH_LongPollResponse_WHITE_CARDS = "wc"
CAH_LongPollResponse_REASON = "qr"
CAH_LongPollResponse_GAME_ID = "gid"
CAH_LongPollResponse_EMOTE = "me"
CAH_LongPollResponse_HAND = "h"
CAH_LongPollResponse_INTERMISSION = "i"
CAH_LongPollResponse_PLAYER_INFO = "pi"
CAH_LongPollResponse_BLACK_CARD = "bc"
CAH_LongPollResponse_WINNING_CARD = "WC"
CAH_LongPollResponse_GAME_STATE = "gs"
CAH_LongPollResponse_NICKNAME = "n"
CAH_LongPollResponse_CARDCAST_DECK_INFO = "cdi"
CAH_LongPollResponse_PLAY_TIMER = "Pt"
CAH_LongPollResponse_MESSAGE = "m"
CAH_LongPollResponse_FROM_ADMIN = "fa"
CAH_LongPollResponse_GAME_INFO = "gi"
CAH_LongPollResponse_ERROR = "e"
CAH_LongPollResponse_EVENT = "E"
CAH_LongPollResponse_FROM = "f"
CAH_LongPollResponse_ERROR_CODE = "ec"
CAH_LongPollResponse_TIMESTAMP = "ts"
CAH_LongPollResponse_ROUND_WINNER = "rw"

CAH_ReconnectNextAction_GAME = "game"
CAH_ReconnectNextAction_NONE = "none"

CAH_WhiteCardData_WRITE_IN = "wi"
CAH_WhiteCardData_TEXT = "T"
CAH_WhiteCardData_ID = "cid"
CAH_WhiteCardData_WATERMARK = "W"