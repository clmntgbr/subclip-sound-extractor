import json
from src.Protobuf.Message_pb2 import Clip, Video


class ProtobufConverter:
    @staticmethod
    def json_to_protobuf(message: str) -> Clip:
        data = json.loads(message)

        clip_data = data["clip"]

        clip = Clip()
        clip.id = clip_data["id"]
        clip.userId = clip_data["userId"]

        if "cover" in clip_data:
            clip.cover = clip_data["cover"]
        
        video = Video()
        video.id = clip_data["originalVideo"]["id"]
        video.name = clip_data["originalVideo"]["name"]
        video.mimeType = clip_data["originalVideo"]["mimeType"]
        video.size = int(clip_data["originalVideo"]["size"])

        video.IsInitialized()
        clip.originalVideo.CopyFrom(video)

        clip.IsInitialized()

        return clip
