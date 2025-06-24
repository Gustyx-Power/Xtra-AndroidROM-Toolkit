import sys
from payload_dumper import main as dump_main

def extract_payload(input_bin, output_dir):
    # Simulastion argv for payload_dumper
    sys.argv = ['payload_dumper.py', '--out', output_dir, input_bin]
    dump_main()