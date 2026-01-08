# ADIF Call Sign Counter

A Python utility for counting unique call signs from amateur radio ADIF log files for a specific date.

## Description

This tool parses ADIF (Amateur Data Interchange Format) files and counts the number of unique call signs contacted on a given date. By default, it uses the current date, but you can specify any date you want to analyze.

## Features

- ✅ Parses standard ADIF format files (.adi, .adif)
- ✅ Counts unique call signs for a specific date
- ✅ Displays sorted list of call signs found
- ✅ Supports optional date argument for historical analysis
- ✅ Case-insensitive call sign handling
- ✅ Proper ADIF field parsing with length validation

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation

1. Download the `adif_counter.py` script
2. Make it executable (optional):
   ```bash
   chmod +x adif_counter.py
   ```

## Usage

### Basic Usage (Current Date)

Count unique call signs for today:

```bash
python adif_counter.py logbook.adi
```

### Specify a Date

Count unique call signs for a specific date:

```bash
python adif_counter.py logbook.adi 20250108
```

or

```bash
python adif_counter.py logbook.adi 2025-01-08
```

**Date Format:** YYYYMMDD or YYYY-MM-DD

### Example Output

```
ADIF File: logbook.adi
Date: 2025-01-08

Unique call signs today: 5

Call signs:
  K1ABC
  N2XYZ
  W3DEF
  W4GHI
  W5JKL
```

## Command Line Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `adif_file` | Yes | Path to the ADIF log file |
| `date` | No | Date to filter (YYYYMMDD or YYYY-MM-DD format). Defaults to current date. |

## ADIF Format

This tool expects standard ADIF files with the following structure:

```
ADIF Export
<ADIF_VER:5>3.1.4
<EOH>

<QSO_DATE:8>20250108<TIME_ON:6>143000<CALL:5>K1ABC<BAND:3>20M<MODE:3>SSB<EOR>
<QSO_DATE:8>20250108<TIME_ON:6>151500<CALL:5>N2XYZ<BAND:3>40M<MODE:2>CW<EOR>
```

**Required Fields:**
- `QSO_DATE` - Date of contact (YYYYMMDD format)
- `CALL` - Call sign of the contacted station

## Error Handling

The script will display helpful error messages for common issues:

- File not found
- Invalid ADIF format
- Missing required fields
- Invalid date format

## Examples

### Count today's contacts
```bash
python adif_counter.py ~/Documents/ham_radio/main_log.adi
```

### Count contacts from a contest day
```bash
python adif_counter.py contest_log.adi 20241225
```

### Count contacts from last week
```bash
python adif_counter.py logbook.adi 2025-01-01
```

## Tips

- Call signs are automatically converted to uppercase for consistency
- Duplicate contacts with the same call sign on the same day are counted only once
- The tool ignores header information and only processes QSO records
- Works with logs exported from popular logging software (Log4OM, WSJT-X, N1MM, etc.)

## Troubleshooting

**Problem:** No call signs found  
**Solution:** Verify your ADIF file has `QSO_DATE` and `CALL` fields, and check the date format

**Problem:** "File not found" error  
**Solution:** Check the file path and ensure the file exists

**Problem:** Incorrect count  
**Solution:** Ensure your ADIF file uses the standard date format (YYYYMMDD)

## License

This tool is provided as-is for amateur radio operators. Feel free to modify and distribute.

## Contributing

Suggestions and improvements are welcome! This is a simple utility tool for the ham radio community.

## Author

Created for amateur radio operators who need to quickly analyze their daily contacts.

73! 📻