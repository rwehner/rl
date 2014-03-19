"""
Read a pcap file and output the seconds
and microseconds from each packet.
"""
import struct

pcap_file='V:\workspace\Python3_Homework08\src\wireshark.bin'
pcap_file_header_fmt="=I2H4I"
pcap_packet_header_fmt="=4I"
timestamps = []

with open(pcap_file, 'rb') as f:
    # skip the file header since we don't use it.
    f.seek(struct.calcsize(pcap_file_header_fmt))
    while True:
        packet_header = f.read(struct.calcsize(pcap_packet_header_fmt))
        if packet_header:
            ts_sec, ts_usec, incl_len, orig_len = struct.unpack(pcap_packet_header_fmt, packet_header)
            timestamps.append((ts_sec, ts_usec))
            # we don't need the actual packet contents, so skip them
            f.seek(orig_len, 1)
        else:
            break

for timestamp in timestamps:
    print("{0} {1}".format(timestamp[0], timestamp[1]))