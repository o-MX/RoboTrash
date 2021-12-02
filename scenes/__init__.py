import scenes.main
import scenes.gameover
import scenes.gameplay
import scenes.story

_scenes = {
    "main": main.Stage,
    "game_over": gameover.Stage,
    "story": story.Stage,
    "gameplay": gameplay.Stage,
}

def get(scene_name, game):
    global _scenes
    if scene_name in _scenes:
        return _scenes[scene_name](game)
    return _scenes["main"](game)
