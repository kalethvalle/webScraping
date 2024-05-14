from flask import (
    Blueprint,
    jsonify
)
bp = Blueprint('spec', __name__)


@bp.route('/swagger.json')
def swagger():
    swag = {
        "openapi": "3.0.0",
        "info": {
            "title": "API tecnical test",
            "description": "Documentación de la API tecnical test",
            "version": "1.0"
        },
        "paths": {
            "/login": {
                "post": {
                    "tags": ["Authentication"],
                    "description": "request Authentication",
                    "requestBody": {
                        "description": "Created issue object",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "username": {
                                            "type": "string"
                                        },
                                        "password": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "successufully operation",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "token": {
                                                "type": "string",
                                                "example": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ8.eyJ1c2VybmFtZSI6ImFkbWluIn0.F5LymIXr29umPedMOVxMbYgtktSy96AwF9dKtP9CyYw"
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "401": {
                            "description": "unautorized operation",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "message": {
                                                "type": "string",
                                                "example": "username or password is incorrect"
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "500": {
                            "description": "unexpected error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "message": {
                                                "type": "string",
                                                "example": "internal server error"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/api/process": {
                "get": {
                    "tags": ["Process"],
                    "summary": "Fetch the full list of process",
                    "description": "Get a list of all precess",
                    "parameters": [
                        {
                            "name": "Authorization",
                            "in": "header",
                            "description": "token authorization request",
                            "required": True,
                            "schema": {
                                "type": "string",
                                "example": "Bearer Cjffbuo0.uyvivtv.iubvv"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "successufully operation",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "process": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "object",
                                                        "properties": {
                                                            "detail": {
                                                                "type": "object",
                                                                "properties": {
                                                                    "Actor/Ofendido": {
                                                                        "type": "string"
                                                                    },
                                                                    "Delito/Asunto": {
                                                                        "type": "string"
                                                                    },
                                                                    "Demandado/Procesado": {
                                                                        "type": "string"
                                                                    },
                                                                    "Fecha ingreso": {
                                                                        "type": "string"
                                                                    },
                                                                    "Judicatura": {
                                                                        "type": "string"
                                                                    },
                                                                    "Materia": {
                                                                        "type": "string"
                                                                    },
                                                                    "No. proceso vinculado": {
                                                                        "type": "string"
                                                                    },
                                                                    "Número de proceso": {
                                                                        "type": "string"
                                                                    },
                                                                    "Tipo de Ingreso": {
                                                                        "type": "string"
                                                                    },
                                                                    "Tipo de acción": {
                                                                        "type": "string"
                                                                    },
                                                                    "actuaciones": {
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "object",
                                                                            "properties": {
                                                                                "description": {
                                                                                    "type": "string"
                                                                                },
                                                                                "fecha_ingreso": {
                                                                                    "type": "string"
                                                                                },
                                                                                "summary": {
                                                                                    "type": "string"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            "id": {
                                                                "type": "string"
                                                            },
                                                            "fecha": {
                                                                "type": "string"
                                                            },
                                                            "infraccion": {
                                                                "type": "string"
                                                            },
                                                            "nro_actor": {
                                                                "type": "string"
                                                            },
                                                            "nro_proceso": {
                                                                "type": "string"
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },

                                    }
                                }
                            }
                        },
                        "400": {
                            "description": "bad request operation",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "message": {
                                                "type": "string",
                                                "example": "Token not attached"
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "401": {
                            "description": "unautorized operation",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "message": {
                                                "type": "string",
                                                "example": "Expired token"
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "403": {
                            "description": "forbiden operation",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "message": {
                                                "type": "string",
                                                "example": "Invalid user"
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "500": {
                            "description": "unexpected error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "message": {
                                                "type": "string",
                                                "example": "internal server error"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
    }
    return jsonify(swag)