import asyncio
import os
import websockets

async def proxy_handler(websocket, path):
    print("Client connected!")
    try:
        async for message in websocket:
            # Hapa mfumo unachakata traffic inayokuja kupitia SNI
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected.")

async def main():
    # Render inatoa PORT kiotomatiki kupitia Environment Variable
    port = int(os.environ.get("PORT", 8080))
    async with websockets.serve(proxy_handler, "0.0.0.0", port):
        print(f"Server inayofanya kazi kama IP imeaswa kwenye port: {port}")
        await asyncio.Future()  # Inafanya server isizime

if __name__ == "__main__":
    asyncio.run(main())
                
