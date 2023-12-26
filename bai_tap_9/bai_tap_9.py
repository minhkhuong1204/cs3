products = ["cat", "banana", "obama", "car", "cow", "alibaba"]
trie = {
    "children": {
        "c": {
            "children": {
                "a": {
                    "children": {
                        "r": {
                            "children": {},
                            "is_end_of_word": True
                        },
                        "t": {
                            "children": {},
                            "is_end_of_word": True
                        }
                    },
                    "is_end_of_word": False
                },
                "o": {
                    "children": {
                        "w": {
                            "children": {},
                            "is_end_of_word": True
                        }
                    },
                    "is_end_of_word": False
                }
            },
            "is_end_of_word": False
        },
        "b": {
            "children": {
                "a": {
                    "children": {
                        "n": {
                            "children": {
                                "a": {
                                    "children": {
                                        "n": {
                                            "children": {
                                                "a": {
                                                    "children": {},
                                                    "is_end_of_word": True
                                                }
                                            },
                                            "is_end_of_word": False
                                        }
                                    },
                                    "is_end_of_word": False
                                }
                            },
                            "is_end_of_word": False
                        }
                    },
                    "is_end_of_word": False
                }
            },
            "is_end_of_word": False
        },
        "o": {
            "children": {
                "b": {
                    "children": {
                        "a": {
                            "children": {
                                "m": {
                                    "children": {
                                        "a": {
                                            "children": {},
                                            "is_end_of_word": True
                                        }
                                    },
                                    "is_end_of_word": False
                                }
                            },
                            "is_end_of_word": False
                        }
                    },
                    "is_end_of_word": False
                }
            },
            "is_end_of_word": False
        }
    },
    "is_end_of_word": False
}
