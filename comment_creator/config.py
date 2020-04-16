import copy
# CONFIG FILE
#
#
# config filename
CONFIG_FILE_NAME = "setting.json"
#
#space definition
SPACE_LEN = 1


def new_cfg():
    """
    function to create the JSON configuration file
    """
    _sl = []
    _sl = {'delimiterSymbol': '',
            'interruptionSymbol': ''}
    _ml = []
    _ml = {'delimiterSymbolBegin': '',
            'delimiterSymbolEnd': '',
            'interruptionSymbol': ''}
    _l = []
    _l = {'Python': {
            'lineLength': '',
            'singleLineSettings': copy.deepcopy(_sl),
            'multiLineSettings': copy.deepcopy(_ml)
            },
            'C': {
            'lineLength': '',
            'singleLineSettings': copy.deepcopy(_sl),
            'multiLineSettings': copy.deepcopy(_ml)
            },
            'Matlab': {
            'lineLength': '',
            'singleLineSettings': copy.deepcopy(_sl),
            'multiLineSettings': copy.deepcopy(_ml)
            }
        }
    cfg = []
    cfg = {'lastSession':\
            {'dialect': 'Python',\
            'upperCase': 'yes',\
            'multiLines': 'no',\
            'frame': 'yes',\
            'centered': 'yes',\
            'copyClipboard': 'yes',\
            'alwaysOnTop': 'no'},\
            'language': _l}
    cfg['language']['Python']['lineLength'] = 72
    cfg['language']['Python']['singleLineSettings']['delimiterSymbol'] = '#'
    cfg['language']['Python']['singleLineSettings']['interruptionSymbol'] = '*'
    cfg['language']['Python']['multiLineSettings']['delimiterSymbolBegin'] = '\"\"\"'
    cfg['language']['Python']['multiLineSettings']['delimiterSymbolEnd'] = '\"\"\"'
    cfg['language']['Python']['multiLineSettings']['interruptionSymbol'] = '*'
    cfg['language']['C']['lineLength'] = 72
    cfg['language']['C']['singleLineSettings']['delimiterSymbol'] = '//'
    cfg['language']['C']['singleLineSettings']['interruptionSymbol'] = '*'
    cfg['language']['C']['multiLineSettings']['delimiterSymbolBegin'] = '/*'
    cfg['language']['C']['multiLineSettings']['delimiterSymbolEnd'] = '*/'
    cfg['language']['C']['multiLineSettings']['interruptionSymbol'] = '*'
    cfg['language']['Matlab']['lineLength'] = 76
    cfg['language']['Matlab']['singleLineSettings']['delimiterSymbol'] = '%'
    cfg['language']['Matlab']['singleLineSettings']['interruptionSymbol'] = '*'
    cfg['language']['Matlab']['multiLineSettings']['delimiterSymbolBegin'] = '%'
    cfg['language']['Matlab']['multiLineSettings']['delimiterSymbolEnd'] = '%'
    cfg['language']['Matlab']['multiLineSettings']['interruptionSymbol'] = '%'
    return cfg


# json schema definition
# built from: https://jsonschema.net/home
configSchema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The Root Schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "additionalProperties": True,
    "required": [
        "lastSession",
        "language"
    ],
    "properties": {
        "lastSession": {
            "$id": "#/properties/lastSession",
            "type": "object",
            "title": "The Lastsession Schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "alwaysOnTop": "no",
                    "dialect": "Python",
                    "multiLines": "no",
                    "centered": "yes",
                    "copyClipboard": "no",
                    "frame": "yes",
                    "upperCase": "yes"
                }
            ],
            "additionalProperties": True,
            "required": [
                "dialect",
                "upperCase",
                "multiLines",
                "frame",
                "centered",
                "copyClipboard",
                "alwaysOnTop"
            ],
            "properties": {
                "dialect": {
                    "$id": "#/properties/lastSession/properties/dialect",
                    "type": "string",
                    "title": "The Dialect Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "Python"
                    ]
                },
                "upperCase": {
                    "$id": "#/properties/lastSession/properties/upperCase",
                    "type": "string",
                    "title": "The Uppercase Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "yes"
                    ]
                },
                "multiLines": {
                    "$id": "#/properties/lastSession/properties/multiLines",
                    "type": "string",
                    "title": "The Multilines Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "no"
                    ]
                },
                "frame": {
                    "$id": "#/properties/lastSession/properties/frame",
                    "type": "string",
                    "title": "The Frame Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "yes"
                    ]
                },
                "centered": {
                    "$id": "#/properties/lastSession/properties/centered",
                    "type": "string",
                    "title": "The Centered Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "yes"
                    ]
                },
                "copyClipboard": {
                    "$id": "#/properties/lastSession/properties/copyClipboard",
                    "type": "string",
                    "title": "The Copyclipboard Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "no"
                    ]
                },
                "alwaysOnTop": {
                    "$id": "#/properties/lastSession/properties/alwaysOnTop",
                    "type": "string",
                    "title": "The Alwaysontop Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "no"
                    ]
                }
            }
        },
        "language": {
            "$id": "#/properties/language",
            "type": "object",
            "title": "The Language Schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "C": {
                        "singleLineSettings": {
                            "interruptionSymbol": "*",
                            "delimiterSymbol": "//"
                        },
                        "multiLineSettings": {
                            "interruptionSymbol": "*",
                            "delimiterSymbolBegin": "/*",
                            "delimiterSymbolEnd": "*/"
                        },
                        "lineLength": 72.0
                    },
                    "Python": {
                        "lineLength": 72.0,
                        "singleLineSettings": {
                            "interruptionSymbol": "*",
                            "delimiterSymbol": "#"
                        },
                        "multiLineSettings": {
                            "interruptionSymbol": "*",
                            "delimiterSymbolBegin": "\"\"\"",
                            "delimiterSymbolEnd": "\"\"\""
                        }
                    },
                    "Matlab": {
                        "lineLength": 76.0,
                        "singleLineSettings": {
                            "interruptionSymbol": "*",
                            "delimiterSymbol": "%"
                        },
                        "multiLineSettings": {
                            "delimiterSymbolBegin": "%",
                            "delimiterSymbolEnd": "%",
                            "interruptionSymbol": "%"
                        }
                    }
                }
            ],
            "additionalProperties": True,
            "required": [
                "Python",
                "C",
                "Matlab"
            ],
            "properties": {
                "Python": {
                    "$id": "#/properties/language/properties/Python",
                    "type": "object",
                    "title": "The Python Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "lineLength": 72.0,
                            "singleLineSettings": {
                                "interruptionSymbol": "*",
                                "delimiterSymbol": "#"
                            },
                            "multiLineSettings": {
                                "interruptionSymbol": "*",
                                "delimiterSymbolBegin": "\"\"\"",
                                "delimiterSymbolEnd": "\"\"\""
                            }
                        }
                    ],
                    "additionalProperties": True,
                    "required": [
                        "lineLength",
                        "singleLineSettings",
                        "multiLineSettings"
                    ],
                    "properties": {
                        "lineLength": {
                            "$id": "#/properties/language/properties/Python/properties/lineLength",
                            "type": "integer",
                            "title": "The Linelength Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                72.0
                            ]
                        },
                        "singleLineSettings": {
                            "$id": "#/properties/language/properties/Python/properties/singleLineSettings",
                            "type": "object",
                            "title": "The Singlelinesettings Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "interruptionSymbol": "*",
                                    "delimiterSymbol": "#"
                                }
                            ],
                            "additionalProperties": True,
                            "required": [
                                "delimiterSymbol",
                                "interruptionSymbol"
                            ],
                            "properties": {
                                "delimiterSymbol": {
                                    "$id": "#/properties/language/properties/Python/properties/singleLineSettings/properties/delimiterSymbol",
                                    "type": "string",
                                    "title": "The Delimitersymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "#"
                                    ]
                                },
                                "interruptionSymbol": {
                                    "$id": "#/properties/language/properties/Python/properties/singleLineSettings/properties/interruptionSymbol",
                                    "type": "string",
                                    "title": "The Interruptionsymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "*"
                                    ]
                                }
                            }
                        },
                        "multiLineSettings": {
                            "$id": "#/properties/language/properties/Python/properties/multiLineSettings",
                            "type": "object",
                            "title": "The Multilinesettings Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "interruptionSymbol": "*",
                                    "delimiterSymbolBegin": "\"\"\"",
                                    "delimiterSymbolEnd": "\"\"\""
                                }
                            ],
                            "additionalProperties": True,
                            "required": [
                                "delimiterSymbolBegin",
                                "delimiterSymbolEnd",
                                "interruptionSymbol"
                            ],
                            "properties": {
                                "delimiterSymbolBegin": {
                                    "$id": "#/properties/language/properties/Python/properties/multiLineSettings/properties/delimiterSymbolBegin",
                                    "type": "string",
                                    "title": "The Delimitersymbolbegin Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "\"\"\""
                                    ]
                                },
                                "delimiterSymbolEnd": {
                                    "$id": "#/properties/language/properties/Python/properties/multiLineSettings/properties/delimiterSymbolEnd",
                                    "type": "string",
                                    "title": "The Delimitersymbolend Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "\"\"\""
                                    ]
                                },
                                "interruptionSymbol": {
                                    "$id": "#/properties/language/properties/Python/properties/multiLineSettings/properties/interruptionSymbol",
                                    "type": "string",
                                    "title": "The Interruptionsymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "*"
                                    ]
                                }
                            }
                        }
                    }
                },
                "C": {
                    "$id": "#/properties/language/properties/C",
                    "type": "object",
                    "title": "The C Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "lineLength": 72.0,
                            "singleLineSettings": {
                                "interruptionSymbol": "*",
                                "delimiterSymbol": "//"
                            },
                            "multiLineSettings": {
                                "interruptionSymbol": "*",
                                "delimiterSymbolBegin": "/*",
                                "delimiterSymbolEnd": "*/"
                            }
                        }
                    ],
                    "additionalProperties": True,
                    "required": [
                        "lineLength",
                        "singleLineSettings",
                        "multiLineSettings"
                    ],
                    "properties": {
                        "lineLength": {
                            "$id": "#/properties/language/properties/C/properties/lineLength",
                            "type": "integer",
                            "title": "The Linelength Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                72.0
                            ]
                        },
                        "singleLineSettings": {
                            "$id": "#/properties/language/properties/C/properties/singleLineSettings",
                            "type": "object",
                            "title": "The Singlelinesettings Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "interruptionSymbol": "*",
                                    "delimiterSymbol": "//"
                                }
                            ],
                            "additionalProperties": True,
                            "required": [
                                "delimiterSymbol",
                                "interruptionSymbol"
                            ],
                            "properties": {
                                "delimiterSymbol": {
                                    "$id": "#/properties/language/properties/C/properties/singleLineSettings/properties/delimiterSymbol",
                                    "type": "string",
                                    "title": "The Delimitersymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "//"
                                    ]
                                },
                                "interruptionSymbol": {
                                    "$id": "#/properties/language/properties/C/properties/singleLineSettings/properties/interruptionSymbol",
                                    "type": "string",
                                    "title": "The Interruptionsymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "*"
                                    ]
                                }
                            }
                        },
                        "multiLineSettings": {
                            "$id": "#/properties/language/properties/C/properties/multiLineSettings",
                            "type": "object",
                            "title": "The Multilinesettings Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "delimiterSymbolEnd": "*/",
                                    "interruptionSymbol": "*",
                                    "delimiterSymbolBegin": "/*"
                                }
                            ],
                            "additionalProperties": True,
                            "required": [
                                "delimiterSymbolBegin",
                                "delimiterSymbolEnd",
                                "interruptionSymbol"
                            ],
                            "properties": {
                                "delimiterSymbolBegin": {
                                    "$id": "#/properties/language/properties/C/properties/multiLineSettings/properties/delimiterSymbolBegin",
                                    "type": "string",
                                    "title": "The Delimitersymbolbegin Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "/*"
                                    ]
                                },
                                "delimiterSymbolEnd": {
                                    "$id": "#/properties/language/properties/C/properties/multiLineSettings/properties/delimiterSymbolEnd",
                                    "type": "string",
                                    "title": "The Delimitersymbolend Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "*/"
                                    ]
                                },
                                "interruptionSymbol": {
                                    "$id": "#/properties/language/properties/C/properties/multiLineSettings/properties/interruptionSymbol",
                                    "type": "string",
                                    "title": "The Interruptionsymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "*"
                                    ]
                                }
                            }
                        }
                    }
                },
                "Matlab": {
                    "$id": "#/properties/language/properties/Matlab",
                    "type": "object",
                    "title": "The Matlab Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "multiLineSettings": {
                                "interruptionSymbol": "%",
                                "delimiterSymbolBegin": "%",
                                "delimiterSymbolEnd": "%"
                            },
                            "lineLength": 76.0,
                            "singleLineSettings": {
                                "interruptionSymbol": "*",
                                "delimiterSymbol": "%"
                            }
                        }
                    ],
                    "additionalProperties": True,
                    "required": [
                        "lineLength",
                        "singleLineSettings",
                        "multiLineSettings"
                    ],
                    "properties": {
                        "lineLength": {
                            "$id": "#/properties/language/properties/Matlab/properties/lineLength",
                            "type": "integer",
                            "title": "The Linelength Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                76.0
                            ]
                        },
                        "singleLineSettings": {
                            "$id": "#/properties/language/properties/Matlab/properties/singleLineSettings",
                            "type": "object",
                            "title": "The Singlelinesettings Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "interruptionSymbol": "*",
                                    "delimiterSymbol": "%"
                                }
                            ],
                            "additionalProperties": True,
                            "required": [
                                "delimiterSymbol",
                                "interruptionSymbol"
                            ],
                            "properties": {
                                "delimiterSymbol": {
                                    "$id": "#/properties/language/properties/Matlab/properties/singleLineSettings/properties/delimiterSymbol",
                                    "type": "string",
                                    "title": "The Delimitersymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "%"
                                    ]
                                },
                                "interruptionSymbol": {
                                    "$id": "#/properties/language/properties/Matlab/properties/singleLineSettings/properties/interruptionSymbol",
                                    "type": "string",
                                    "title": "The Interruptionsymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "*"
                                    ]
                                }
                            }
                        },
                        "multiLineSettings": {
                            "$id": "#/properties/language/properties/Matlab/properties/multiLineSettings",
                            "type": "object",
                            "title": "The Multilinesettings Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "interruptionSymbol": "%",
                                    "delimiterSymbolBegin": "%",
                                    "delimiterSymbolEnd": "%"
                                }
                            ],
                            "additionalProperties": True,
                            "required": [
                                "delimiterSymbolBegin",
                                "delimiterSymbolEnd",
                                "interruptionSymbol"
                            ],
                            "properties": {
                                "delimiterSymbolBegin": {
                                    "$id": "#/properties/language/properties/Matlab/properties/multiLineSettings/properties/delimiterSymbolBegin",
                                    "type": "string",
                                    "title": "The Delimitersymbolbegin Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "%"
                                    ]
                                },
                                "delimiterSymbolEnd": {
                                    "$id": "#/properties/language/properties/Matlab/properties/multiLineSettings/properties/delimiterSymbolEnd",
                                    "type": "string",
                                    "title": "The Delimitersymbolend Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "%"
                                    ]
                                },
                                "interruptionSymbol": {
                                    "$id": "#/properties/language/properties/Matlab/properties/multiLineSettings/properties/interruptionSymbol",
                                    "type": "string",
                                    "title": "The Interruptionsymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "%"
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
