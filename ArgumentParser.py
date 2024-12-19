import argparse
import asyncio
import logging
from aiopath import AsyncPath
from aioshutil import copy

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def read_folder(source: AsyncPath, output: AsyncPath):
    
    if not await source.exists():
        logger.error(f"Source folder '{source}' does not exist.")
        return

    if not await output.exists():
        await output.mkdir(parents=True)

    async for item in source.iterdir():
        if await item.is_dir():
            await read_folder(item, output)
        elif await item.is_file():
            await copy_file(item, output)

async def copy_file(file: AsyncPath, output: AsyncPath):
    
    extension = file.suffix.lstrip(".") or "unknown"
    target_folder = output / extension

    if not await target_folder.exists():
        await target_folder.mkdir(parents=True)

    target_file = target_folder / file.name

    try:
        await copy(file, target_file)
        logger.info(f"Copied: {file} -> {target_file}")
    except Exception as e:
        logger.error(f"Failed to copy {file}: {e}")

def parse_args():
    
    parser = argparse.ArgumentParser(description="Asynchronous file sorting script.")
    parser.add_argument("source", type=str, help="Path to the source folder.")
    parser.add_argument("output", type=str, help="Path to the output folder.")
    return parser.parse_args()

async def main():
    args = parse_args()
    source = AsyncPath(args.source)
    output = AsyncPath(args.output)

    logger.info("Starting file sorting...")
    await read_folder(source, output)
    logger.info("File sorting completed.")

if __name__ == "__main__":
    asyncio.run(main())
