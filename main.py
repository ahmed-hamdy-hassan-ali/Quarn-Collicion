from flet import *
import flet_audio as fa
import os



async def main(page:Page):
    page.scroll=ScrollMode.ALWAYS
    def play(e:Event):
        if any(page.services):
            page.services.clear()
        page.services.append(fa.Audio(
            release_mode=fa.ReleaseMode.LOOP,
            src=e.control.content+".mp3",autoplay=True)
            )
        page.update()
    page.add(Image("shiekh.png"))
    for file in os.listdir("assets"):
        if ".mp3" not in file:
            continue
        page.add(TextButton(
            os.path.splitext(file)[0],
            width=1500,
            style=ButtonStyle(shape=RoundedRectangleBorder()),
            on_click=play
            ),
            Divider()
            )
    page.update()
    

run(main)
