"""
Simple demonstration of the meta-creation concept.

This shows how the Creator can:
1. Read its own source code
2. Create new Creator variants
3. Have those new Creators create their own agents

Run this after running meta_world.py to see the results!
"""

from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntimeHost
from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntime
from creator import Creator
from autogen_core import AgentId
import messages
import asyncio


async def simple_meta_test():
    """Simple test: Original Creator creates ONE new Creator"""
    host = GrpcWorkerAgentRuntimeHost(address="localhost:50053")
    host.start()
    worker = GrpcWorkerAgentRuntime(host_address="localhost:50053")
    await worker.start()

    # Register the original Creator
    result = await Creator.register(worker, "Creator", lambda: Creator("Creator"))
    creator_id = AgentId("Creator", "default")

    print("\n" + "="*80)
    print("SIMPLE META-CREATION TEST")
    print("="*80)
    print("\nStep 1: Original Creator reads its own code (creator.py)")
    print("Step 2: Original Creator creates a specialized Creator")
    print("Step 3: New Creator creates its own agent")
    print("="*80 + "\n")

    # Create ONE new Creator
    result = await worker.send_message(
        messages.Message(content="creator_specialist.py"),
        creator_id
    )

    print(f"\n{'='*80}")
    print("RESULT:")
    print(f"{'='*80}")
    print(result.content)
    print(f"{'='*80}\n")

    # Save result
    with open("meta_test_result.md", "w") as f:
        f.write("# Meta-Creation Test Result\n\n")
        f.write(result.content)

    print("\n✓ Check these files:")
    print("  - creator_specialist.py (the new Creator)")
    print("  - creator_specialist_agent1.py (agent created by the new Creator)")
    print("  - meta_test_result.md (detailed result)\n")

    try:
        await worker.stop()
        await host.stop()
    except Exception as e:
        print(e)


async def chain_test():
    """Advanced test: Create a Creator that creates a Creator!"""
    host = GrpcWorkerAgentRuntimeHost(address="localhost:50054")
    host.start()
    worker = GrpcWorkerAgentRuntime(host_address="localhost:50054")
    await worker.start()

    # Register the original Creator
    await Creator.register(worker, "Creator", lambda: Creator("Creator"))
    creator_id = AgentId("Creator", "default")

    print("\n" + "="*80)
    print("CHAIN META-CREATION TEST (Creator → Creator → Agent)")
    print("="*80 + "\n")

    # Step 1: Creator creates Creator2
    print("Step 1: Creator creates Creator2...")
    result1 = await worker.send_message(
        messages.Message(content="creator2.py"),
        creator_id
    )
    print(f"✓ {result1.content}\n")

    # Step 2: Creator2 creates Creator3
    print("Step 2: Creator2 creates Creator3...")
    creator2_id = AgentId("creator2", "default")
    result2 = await worker.send_message(
        messages.Message(content="creator3.py"),
        creator2_id
    )
    print(f"✓ {result2.content}\n")

    # Step 3: Creator3 creates an agent
    print("Step 3: Creator3 creates an agent...")
    creator3_id = AgentId("creator3", "default")
    result3 = await worker.send_message(
        messages.Message(content="final_agent.py"),
        creator3_id
    )
    print(f"✓ {result3.content}\n")

    print("="*80)
    print("CHAIN COMPLETE!")
    print("Creator → Creator2 → Creator3 → Agent")
    print("="*80 + "\n")

    try:
        await worker.stop()
        await host.stop()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "chain":
        print("\n🌀 Running CHAIN test (Creator creates Creator creates Creator)...\n")
        asyncio.run(chain_test())
    else:
        print("\n🌀 Running SIMPLE test (Creator creates Creator)...\n")
        print("💡 Tip: Run with 'python simple_meta_test.py chain' for the chain test\n")
        asyncio.run(simple_meta_test())
