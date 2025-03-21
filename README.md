# num2label

A package to map numbers to text labels. For example, `n` maps to the `nth` letter of the alphabet. You can also map numbers to their corresponding spreadsheet column labels.

## Quick start

To get started, import `num2label`:

```python3
>>> import num2label
```

### Integer to letter

Map an integer to an uppercase letter of the alphabet:

```python3
>>> num2label.uppercase_letter(1)
'A'
```

Or a lowercase letter:

```python3
>>> num2label.lowercase_letter(26)
'z'
```

### Integer to spreadsheet column label

Map a number to a spreadsheet column label:

```python3
>>> num2label.spreadsheet_column(28)
'AB'
```

## Number bounds

The number must always be greater than zero. The number can be greater than 26. `uppercase_letter` and `lowercase_letter` will effectively loop the alphabet until the corresponding letter is reached (e.g., `27 => 'a'`, `55 => 'C'`). To ensure the number passed is strictly less than 27, pass `strict=True`. `num2label.lowercase_letter(27, strict=True)` will raise an error because the number is not between one and 26 (inclusive).
