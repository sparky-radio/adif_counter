#!/usr/bin/env python3
"""
ADIF Call Sign Counter
Counts unique call signs from an ADIF file for the current day.
"""

import re
from datetime import datetime, timezone, UTC
from pathlib import Path

HOME='/home/k5aq/Documents/WSJT-X/logs/'

def parse_adif_file(filename):
    """Parse ADIF file and extract QSO records."""
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find the end of header (marked by <EOH> or <eoh>)
    eoh_match = re.search(r'<EOH>', content, re.IGNORECASE)
    if eoh_match:
        content = content[eoh_match.end():]
    
    # Split into individual QSO records (marked by <EOR> or <eor>)
    records = re.split(r'<EOR>', content, flags=re.IGNORECASE)
    
    qsos = []
    for record in records:
        if not record.strip():
            continue
        
        qso = {}
        # Find all ADIF fields in format <FIELD:LENGTH>VALUE or <FIELD:LENGTH:TYPE>VALUE
        fields = re.findall(r'<([^:>]+):(\d+)(?::([^>]+))?>([^<]*)', record, re.IGNORECASE)
        
        for field_name, length, data_type, value in fields:
            field_name = field_name.upper()
            length = int(length)
            # Extract only the specified length of characters
            qso[field_name] = value[:length]
        
        if qso:
            qsos.append(qso)
    
    return qsos


def count_unique_callsigns_today(filename, today):
    """Count unique call signs for the current day."""
    qsos = parse_adif_file(filename)

    
    unique_callsigns = set()
    
    for qso in qsos:
        qso_date = qso.get('QSO_DATE', '')
        callsign = qso.get('CALL', '')
        
        # Check if this QSO is from today
        if qso_date == today and callsign:
            unique_callsigns.add(callsign.upper())
    
    return unique_callsigns


def main():
    """Main function."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python adif_counter.py <adif_file> <YYYYMMDD optional>")
        print("Example: python adif_counter.py logbook.adi")
        sys.exit(1)
    
    filename = sys.argv[1]
    filename = HOME + filename


    # Get today's date in YYYYMMDD format
    today = datetime.now(UTC).strftime('%Y%m%d')
    if len(sys.argv) > 2:
        naive_dt = datetime.strptime(sys.argv[2],  '%Y%m%d')
        today = naive_dt.replace(tzinfo=timezone.utc).strftime('%Y%m%d')
    
    if not Path(filename).exists():
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    try:
        unique_callsigns = count_unique_callsigns_today(filename, today)
        
        print(f"\nADIF File: {filename}")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
        print(f"\nUnique call signs today: {len(unique_callsigns)}")
        
        if unique_callsigns:
            print("\nCall signs:")
            for callsign in sorted(unique_callsigns):
                print(f"  {callsign}")
    
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()