import scenes.main
import scenes.gameover
import scenes.gameplay
import scenes.story

_scenes = {
    "main": main.Scene,
    "gameover": gameover.Scene,
    "story": story.Scene,
    "gameplay": gameplay.Scene,
}

def get(scene_name):
    global _scenes
    if scene_name in _scenes:
        return _scenes[scene_name]()
    return _scenes["main"]()
