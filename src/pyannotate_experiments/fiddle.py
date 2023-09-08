from pyannote.audio import Pipeline

pipeline = Pipeline.from_pretrained("pyannote/voice-activity-detection",
                                    use_auth_token="ACCESS_TOKEN_GOES_HERE")