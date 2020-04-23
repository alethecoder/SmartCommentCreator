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
            'interruptionSymbol': '',
            'frameOnDelimiter': '',
            'framePositionBegin': ''}
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
    cfg['language']['Python']['multiLineSettings']['needDelimiter'] = 'no'
    cfg['language']['Python']['multiLineSettings']['interruptionSymbol'] = '*'
    cfg['language']['Python']['multiLineSettings']['frameOnDelimiter'] = 'no'
    cfg['language']['Python']['multiLineSettings']['frameOffset'] = 4
    cfg['language']['C']['lineLength'] = 72
    cfg['language']['C']['singleLineSettings']['delimiterSymbol'] = '//'
    cfg['language']['C']['singleLineSettings']['interruptionSymbol'] = '*'
    cfg['language']['C']['multiLineSettings']['delimiterSymbolBegin'] = '/*'
    cfg['language']['C']['multiLineSettings']['delimiterSymbolEnd'] = '*/'
    cfg['language']['C']['multiLineSettings']['needDelimiter'] = 'no'
    cfg['language']['C']['multiLineSettings']['interruptionSymbol'] = '*'
    cfg['language']['C']['multiLineSettings']['frameOnDelimiter'] = 'yes'
    cfg['language']['C']['multiLineSettings']['frameOffset'] = 2
    cfg['language']['Matlab']['lineLength'] = 76
    cfg['language']['Matlab']['singleLineSettings']['delimiterSymbol'] = '%'
    cfg['language']['Matlab']['singleLineSettings']['interruptionSymbol'] = '*'
    cfg['language']['Matlab']['multiLineSettings']['delimiterSymbolBegin'] = '%'
    cfg['language']['Matlab']['multiLineSettings']['delimiterSymbolEnd'] = '%'
    cfg['language']['Matlab']['multiLineSettings']['needDelimiter'] = 'yes'
    cfg['language']['Matlab']['multiLineSettings']['interruptionSymbol'] = '%'
    cfg['language']['Matlab']['multiLineSettings']['frameOnDelimiter'] = 'yes'
    cfg['language']['Matlab']['multiLineSettings']['frameOffset'] = 1
    return cfg


# json schema definition
# built from: https://jsonschema.net/home
configSchema = {
    "$schema": "http://json-schema.org/draft-07/schema",
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
            "type": "object",
            "title": "The Lastsession Schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "upperCase": "yes",
                    "alwaysOnTop": "no",
                    "dialect": "Python",
                    "multiLines": "no",
                    "centered": "yes",
                    "copyClipboard": "yes",
                    "frame": "yes"
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
                    "type": "string",
                    "title": "The Dialect Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "Python"
                    ]
                },
                "upperCase": {
                    "type": "string",
                    "title": "The Uppercase Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "yes"
                    ]
                },
                "multiLines": {
                    "type": "string",
                    "title": "The Multilines Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "no"
                    ]
                },
                "frame": {
                    "type": "string",
                    "title": "The Frame Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "yes"
                    ]
                },
                "centered": {
                    "type": "string",
                    "title": "The Centered Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "yes"
                    ]
                },
                "copyClipboard": {
                    "type": "string",
                    "title": "The Copyclipboard Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "yes"
                    ]
                },
                "alwaysOnTop": {
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
            "type": "object",
            "title": "The Language Schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "Python": {
                        "lineLength": 72.0,
                        "singleLineSettings": {
                            "delimiterSymbol": "#",
                            "interruptionSymbol": "*"
                        },
                        "multiLineSettings": {
                            "frameOffset": 4.0,
                            "frameOnDelimiter": "no",
                            "needDelimiter": "no",
                            "interruptionSymbol": "*",
                            "delimiterSymbolBegin": "\"\"\"",
                            "delimiterSymbolEnd": "\"\"\"",
                            "framePositionBegin": ""
                        }
                    },
                    "Matlab": {
                        "lineLength": 76.0,
                        "singleLineSettings": {
                            "delimiterSymbol": "%",
                            "interruptionSymbol": "*"
                        },
                        "multiLineSettings": {
                            "needDelimiter": "yes",
                            "frameOnDelimiter": "yes",
                            "interruptionSymbol": "%",
                            "delimiterSymbolBegin": "%",
                            "delimiterSymbolEnd": "%",
                            "framePositionBegin": "",
                            "frameOffset": 2.0
                        }
                    },
                    "C": {
                        "singleLineSettings": {
                            "delimiterSymbol": "//",
                            "interruptionSymbol": "*"
                        },
                        "multiLineSettings": {
                            "needDelimiter": "no",
                            "frameOnDelimiter": "yes",
                            "interruptionSymbol": "*",
                            "delimiterSymbolBegin": "/*",
                            "delimiterSymbolEnd": "*/",
                            "framePositionBegin": "",
                            "frameOffset": 2.0
                        },
                        "lineLength": 72.0
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
                    "type": "object",
                    "title": "The Python Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "lineLength": 72.0,
                            "singleLineSettings": {
                                "delimiterSymbol": "#",
                                "interruptionSymbol": "*"
                            },
                            "multiLineSettings": {
                                "framePositionBegin": "",
                                "frameOffset": 4.0,
                                "needDelimiter": "no",
                                "frameOnDelimiter": "no",
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
                            "type": "integer",
                            "title": "The Linelength Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                72.0
                            ]
                        },
                        "singleLineSettings": {
                            "type": "object",
                            "title": "The Singlelinesettings Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "delimiterSymbol": "#",
                                    "interruptionSymbol": "*"
                                }
                            ],
                            "additionalProperties": True,
                            "required": [
                                "delimiterSymbol",
                                "interruptionSymbol"
                            ],
                            "properties": {
                                "delimiterSymbol": {
                                    "type": "string",
                                    "title": "The Delimitersymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "#"
                                    ]
                                },
                                "interruptionSymbol": {
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
                            "type": "object",
                            "title": "The Multilinesettings Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "delimiterSymbolBegin": "\"\"\"",
                                    "delimiterSymbolEnd": "\"\"\"",
                                    "framePositionBegin": "",
                                    "frameOffset": 4.0,
                                    "frameOnDelimiter": "no",
                                    "needDelimiter": "no",
                                    "interruptionSymbol": "*"
                                }
                            ],
                            "additionalProperties": True,
                            "required": [
                                "delimiterSymbolBegin",
                                "delimiterSymbolEnd",
                                "interruptionSymbol",
                                "frameOnDelimiter",
                                "framePositionBegin",
                                "needDelimiter",
                                "frameOffset"
                            ],
                            "properties": {
                                "delimiterSymbolBegin": {
                                    "type": "string",
                                    "title": "The Delimitersymbolbegin Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "\"\"\""
                                    ]
                                },
                                "delimiterSymbolEnd": {
                                    "type": "string",
                                    "title": "The Delimitersymbolend Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "\"\"\""
                                    ]
                                },
                                "interruptionSymbol": {
                                    "type": "string",
                                    "title": "The Interruptionsymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "*"
                                    ]
                                },
                                "frameOnDelimiter": {
                                    "type": "string",
                                    "title": "The Frameondelimiter Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "no"
                                    ]
                                },
                                "framePositionBegin": {
                                    "type": "string",
                                    "title": "The Framepositionbegin Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        ""
                                    ]
                                },
                                "needDelimiter": {
                                    "type": "string",
                                    "title": "The Needdelimiter Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "no"
                                    ]
                                },
                                "frameOffset": {
                                    "type": "integer",
                                    "title": "The Frameoffset Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": 0,
                                    "examples": [
                                        4.0
                                    ]
                                }
                            }
                        }
                    }
                },
                "C": {
                    "type": "object",
                    "title": "The C Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "lineLength": 72.0,
                            "singleLineSettings": {
                                "delimiterSymbol": "//",
                                "interruptionSymbol": "*"
                            },
                            "multiLineSettings": {
                                "delimiterSymbolEnd": "*/",
                                "framePositionBegin": "",
                                "frameOffset": 2.0,
                                "needDelimiter": "no",
                                "frameOnDelimiter": "yes",
                                "interruptionSymbol": "*",
                                "delimiterSymbolBegin": "/*"
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
                            "type": "integer",
                            "title": "The Linelength Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                72.0
                            ]
                        },
                        "singleLineSettings": {
                            "type": "object",
                            "title": "The Singlelinesettings Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "delimiterSymbol": "//",
                                    "interruptionSymbol": "*"
                                }
                            ],
                            "additionalProperties": True,
                            "required": [
                                "delimiterSymbol",
                                "interruptionSymbol"
                            ],
                            "properties": {
                                "delimiterSymbol": {
                                    "type": "string",
                                    "title": "The Delimitersymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "//"
                                    ]
                                },
                                "interruptionSymbol": {
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
                            "type": "object",
                            "title": "The Multilinesettings Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "needDelimiter": "no",
                                    "frameOnDelimiter": "yes",
                                    "interruptionSymbol": "*",
                                    "delimiterSymbolBegin": "/*",
                                    "delimiterSymbolEnd": "*/",
                                    "framePositionBegin": "",
                                    "frameOffset": 2.0
                                }
                            ],
                            "additionalProperties": True,
                            "required": [
                                "delimiterSymbolBegin",
                                "delimiterSymbolEnd",
                                "interruptionSymbol",
                                "frameOnDelimiter",
                                "framePositionBegin",
                                "needDelimiter",
                                "frameOffset"
                            ],
                            "properties": {
                                "delimiterSymbolBegin": {
                                    "type": "string",
                                    "title": "The Delimitersymbolbegin Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "/*"
                                    ]
                                },
                                "delimiterSymbolEnd": {
                                    "type": "string",
                                    "title": "The Delimitersymbolend Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "*/"
                                    ]
                                },
                                "interruptionSymbol": {
                                    "type": "string",
                                    "title": "The Interruptionsymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "*"
                                    ]
                                },
                                "frameOnDelimiter": {
                                    "type": "string",
                                    "title": "The Frameondelimiter Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "yes"
                                    ]
                                },
                                "framePositionBegin": {
                                    "type": "string",
                                    "title": "The Framepositionbegin Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        ""
                                    ]
                                },
                                "needDelimiter": {
                                    "type": "string",
                                    "title": "The Needdelimiter Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "no"
                                    ]
                                },
                                "frameOffset": {
                                    "type": "integer",
                                    "title": "The Frameoffset Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": 0,
                                    "examples": [
                                        2.0
                                    ]
                                }
                            }
                        }
                    }
                },
                "Matlab": {
                    "type": "object",
                    "title": "The Matlab Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "lineLength": 76.0,
                            "singleLineSettings": {
                                "delimiterSymbol": "%",
                                "interruptionSymbol": "*"
                            },
                            "multiLineSettings": {
                                "frameOffset": 2.0,
                                "needDelimiter": "yes",
                                "frameOnDelimiter": "yes",
                                "interruptionSymbol": "%",
                                "delimiterSymbolBegin": "%",
                                "delimiterSymbolEnd": "%",
                                "framePositionBegin": ""
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
                            "type": "integer",
                            "title": "The Linelength Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                76.0
                            ]
                        },
                        "singleLineSettings": {
                            "type": "object",
                            "title": "The Singlelinesettings Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "delimiterSymbol": "%",
                                    "interruptionSymbol": "*"
                                }
                            ],
                            "additionalProperties": True,
                            "required": [
                                "delimiterSymbol",
                                "interruptionSymbol"
                            ],
                            "properties": {
                                "delimiterSymbol": {
                                    "type": "string",
                                    "title": "The Delimitersymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "%"
                                    ]
                                },
                                "interruptionSymbol": {
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
                            "type": "object",
                            "title": "The Multilinesettings Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "framePositionBegin": "",
                                    "frameOffset": 2.0,
                                    "needDelimiter": "yes",
                                    "frameOnDelimiter": "yes",
                                    "interruptionSymbol": "%",
                                    "delimiterSymbolBegin": "%",
                                    "delimiterSymbolEnd": "%"
                                }
                            ],
                            "additionalProperties": True,
                            "required": [
                                "delimiterSymbolBegin",
                                "delimiterSymbolEnd",
                                "interruptionSymbol",
                                "frameOnDelimiter",
                                "framePositionBegin",
                                "needDelimiter",
                                "frameOffset"
                            ],
                            "properties": {
                                "delimiterSymbolBegin": {
                                    "type": "string",
                                    "title": "The Delimitersymbolbegin Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "%"
                                    ]
                                },
                                "delimiterSymbolEnd": {
                                    "type": "string",
                                    "title": "The Delimitersymbolend Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "%"
                                    ]
                                },
                                "interruptionSymbol": {
                                    "type": "string",
                                    "title": "The Interruptionsymbol Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "%"
                                    ]
                                },
                                "frameOnDelimiter": {
                                    "type": "string",
                                    "title": "The Frameondelimiter Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "yes"
                                    ]
                                },
                                "framePositionBegin": {
                                    "type": "string",
                                    "title": "The Framepositionbegin Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        ""
                                    ]
                                },
                                "needDelimiter": {
                                    "type": "string",
                                    "title": "The Needdelimiter Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "yes"
                                    ]
                                },
                                "frameOffset": {
                                    "type": "integer",
                                    "title": "The Frameoffset Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": 0,
                                    "examples": [
                                        2.0
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
