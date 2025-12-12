import asyncio
from aiocoap import resource, Message, Context
from aiocoap.numbers.codes import Code
import datetime

class TimeResource(resource.Resource):
    async def render_get(self, request):
        current_time = str(datetime.datetime.now())
        payload = f"Current Time: {current_time}".encode("utf-8")
        return Message(code=Code.CONTENT, payload=payload)

async def main():
    root = resource.Site()
    root.add_resource(['time'], TimeResource())

    await Context.create_server_context(root, bind=("127.0.0.1", 5683))
    print("CoAP Server Running at coap://127.0.0.1/time")

    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())