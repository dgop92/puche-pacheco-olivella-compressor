import logging
import pickle
import time

from core.dahuffman import HuffmanCodec


def decompress_file(compressed_file: str, output_file: str):
    with open(compressed_file, "rb") as file:
        logging.info(f"Reading {compressed_file}")
        compress_data = pickle.load(file)
        codec = HuffmanCodec.create_from_data(compress_data["codec_data"])

        logging.info(f"Decompressing {compressed_file} to {output_file}")
        decoded_parts = []
        for encoded in compress_data["encoded"]:
            decoded_parts.append(codec.decode(encoded))

        decoded = b"".join(decoded_parts)

        with open(output_file, "wb") as file:
            logging.info(f"Writing to {output_file}")
            file.write(decoded)


def decompress_file_logging_time(compressed_file: str, output_file: str):
    start = time.time()
    decompress_file(compressed_file, output_file)
    end = time.time()
    print(end - start)
