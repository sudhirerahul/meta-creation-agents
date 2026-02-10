from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntimeHost
from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntime
from creator import Creator
from autogen_core import AgentId
import messages
import asyncio

"""
Meta-World: Where Creators create Creators!

This demonstrates the meta-creation capability:
1. The original Creator creates new Creator variants
2. Each new Creator can then create its own agents
3. Creators can have different specializations and logic
"""

async def main():
    host = GrpcWorkerAgentRuntimeHost(address="localhost:50052")
    host.start()
    worker = GrpcWorkerAgentRuntime(host_address="localhost:50052")
    await worker.start()

    # Register the original Creator
    result = await Creator.register(worker, "Creator", lambda: Creator("Creator"))
    creator_id = AgentId("Creator", "default")

    print("\n" + "="*80)
    print("META-CREATION DEMO: Creator creating Creators!")
    print("="*80 + "\n")

    # Create a few new Creator variants
    creator_variants = [
        "creator_analytical.py",    # Will specialize in analytical agents
        "creator_creative.py",       # Will specialize in creative agents
        "creator_experimental.py"    # Will be highly experimental
    ]

    for variant_file in creator_variants:
        print(f"\n{'*'*60}")
        print(f"Creating new Creator: {variant_file}")
        print(f"{'*'*60}\n")

        result = await worker.send_message(
            messages.Message(content=variant_file),
            creator_id
        )

        print(f"\n✓ Result: {result.content}\n")

        # Save the result
        variant_name = variant_file.split(".")[0]
        with open(f"{variant_name}_result.md", "w") as f:
            f.write(f"# {variant_name}\n\n")
            f.write(result.content)

    print("\n" + "="*80)
    print("Meta-creation complete! Each new Creator can now create its own agents.")
    print("="*80 + "\n")

    try:
        await worker.stop()
        await host.stop()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())
