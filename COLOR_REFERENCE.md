# 🎨 Quick Color Reference Card

## Copy-Paste Ready Color Values

### Backgrounds
```css
#0a0e27  /* Primary Background - Deep Indigo */
#1a1f3a  /* Secondary Background - Slate Indigo */
#0f1629  /* Tertiary Background - Dark Navy */
rgba(30, 41, 59, 0.75)  /* Card Background */
rgba(15, 23, 42, 0.6)   /* Input Background */
```

### Primary Colors (Cyan/Teal)
```css
#06b6d4  /* Primary Action */
#0891b2  /* Hover State */
#0e7490  /* Pressed State */
#22d3ee  /* Link Color */
#67e8f9  /* Link Hover */
```

### Text Colors
```css
#ffffff  /* Headings - Pure White */
#f1f5f9  /* Body Text - Off White */
#e2e8f0  /* Secondary Text - Light Gray */
#cbd5e1  /* Tertiary Text - Gray */
#94a3b8  /* Muted/Placeholder - Subtle Gray */
```

### Borders
```css
#334155  /* Default Border - Slate Gray */
#475569  /* Hover Border - Medium Gray */
#06b6d4  /* Focus Border - Primary Cyan */
rgba(100, 116, 139, 0.25)  /* Subtle Border */
```

### Feedback
```css
/* Success */
#10b981  /* Emerald Green */
rgba(16, 185, 129, 0.1)  /* Success Background */

/* Error */
#fb7185  /* Rose Red */
rgba(251, 113, 133, 0.1)  /* Error Background */

/* Disabled */
#334155  /* Disabled Background */
#64748b  /* Disabled Text */
```

### Shadows
```css
/* Card Shadow */
blur-radius: 50px
offset: 0, 20px
color: rgba(10, 14, 39, 0.78)
```

---

## Quick Usage Examples

### Button
```python
"QPushButton {"
"  background-color: #06b6d4;"  # Primary cyan
"  color: #ffffff;"              # White text
"  padding: 14px 24px;"
"  border-radius: 10px;"
"}"
"QPushButton:hover {"
"  background-color: #0891b2;"  # Darker on hover
"}"
```

### Input Field
```python
"QLineEdit {"
"  background-color: rgba(15, 23, 42, 0.6);"
"  border: 1.5px solid #334155;"
"  color: #f1f5f9;"
"}"
"QLineEdit:focus {"
"  border: 1.5px solid #06b6d4;"  # Cyan focus border
"}"
```

### Card/Frame
```python
"QFrame {"
"  background-color: rgba(30, 41, 59, 0.75);"
"  border-radius: 20px;"
"  border: 1px solid rgba(100, 116, 139, 0.25);"
"}"
```

### Error Label
```python
"#errorLabel {"
"  color: #fb7185;"
"  background-color: rgba(251, 113, 133, 0.1);"
"  border-radius: 6px;"
"  padding: 8px 12px;"
"}"
```

---

## RGB Values (for QColor)

| Color | RGB | Usage |
|-------|-----|-------|
| Background | `10, 14, 39` | Main background |
| Card | `30, 41, 59` | Card surfaces |
| Primary | `6, 182, 212` | Buttons, links |
| White Text | `255, 255, 255` | Headings |
| Off-White | `241, 245, 249` | Body text |
| Success | `16, 185, 129` | Success messages |
| Error | `251, 113, 133` | Error messages |

---

## Color Naming Convention

- **Primary**: Main action color (cyan #06b6d4)
- **Secondary**: Card/surface colors
- **Accent**: Link colors, highlights
- **Text**: Hierarchical text colors
- **Border**: Element boundaries
- **Feedback**: Success, error, warning states
- **Disabled**: Inactive element states

---

**Pro Tip**: Use this card as a reference when extending the UI or creating new components. All colors are tested for contrast and consistency!

