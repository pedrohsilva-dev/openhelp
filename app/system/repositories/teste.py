from .follows_repository import FollowRepository


followRepository = FollowRepository()


followRepository.object = Follow()
followRepository.delete_object()
