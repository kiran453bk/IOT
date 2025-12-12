import asyncio
from aiocoap import *

async def main():
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri="coap://127.0.0.1/time")

    print("Sending CoAP GET request...")
    response = await protocol.request(request).response

    print("Response Code:", response.code)
    print("Payload:", response.payload.decode())

if __name__ == "__main__":
    asyncio.run(main())