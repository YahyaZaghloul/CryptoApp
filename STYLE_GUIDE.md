# CryptoApp UI Style Guide

## 🎨 Color Palette

### Background Colors
- **Primary Background**: `#0a0e27` (Deep Indigo)
- **Secondary Background**: `#1a1f3a` (Slate Indigo)
- **Tertiary Background**: `#0f1629` (Dark Navy)
- **Gradient**: Linear gradient from `#0a0e27` → `#1a1f3a` → `#0f1629`

### Card & Surface Colors
- **Card Background**: `rgba(30, 41, 59, 0.75)` (Semi-transparent Slate)
- **Card Border**: `rgba(100, 116, 139, 0.25)` (Subtle Gray)
- **Glass Card**: `rgba(30, 41, 59, 0.65)` (More transparent for home)
- **Input Background**: `rgba(15, 23, 42, 0.5)` (Dark translucent)
- **Input Background Hover**: `rgba(30, 41, 59, 0.6)`
- **Input Background Focus**: `rgba(30, 41, 59, 0.7)`

### Primary Action Colors (Teal/Cyan)
- **Primary**: `#06b6d4` (Vibrant Cyan)
- **Primary Hover**: `#0891b2` (Darker Cyan)
- **Primary Pressed**: `#0e7490` (Deep Teal)
- **Link**: `#22d3ee` (Bright Cyan)
- **Link Hover**: `#67e8f9` (Light Cyan)

### Text Colors
- **Primary Text**: `#ffffff` (Pure White for headings)
- **Secondary Text**: `#f1f5f9` (Off-White)
- **Tertiary Text**: `#e2e8f0` (Light Gray)
- **Muted Text**: `#cbd5e1` (Gray)
- **Placeholder Text**: `#94a3b8` (Subtle Gray)

### Border Colors
- **Default**: `#334155` (Slate Gray)
- **Hover**: `#475569` (Medium Gray)
- **Focus**: `#06b6d4` (Primary Cyan)
- **Subtle**: `rgba(100, 116, 139, 0.3)`

### Feedback Colors
- **Success**: `#10b981` (Emerald Green)
- **Success Background**: `rgba(16, 185, 129, 0.1)`
- **Success Border**: `rgba(16, 185, 129, 0.3)`
- **Error**: `#fb7185` (Rose Red)
- **Error Background**: `rgba(251, 113, 133, 0.1)`
- **Disabled**: `#334155` (Dark Gray)
- **Disabled Text**: `#64748b` (Muted Gray)

## 📐 Design Tokens

### Border Radius
- **Small**: `6px` (Labels, tags)
- **Medium**: `10px` (Buttons, inputs)
- **Large**: `16px` (Tables)
- **Extra Large**: `20px` (Cards)
- **XXL**: `24px` (Auth cards)

### Spacing & Padding
- **Button**: `14px 24px`
- **Input**: `14px 16px` (vertical horizontal)
- **Card**: `20px`
- **Card Margins**: `40px`

### Typography
- **Title**: 28-32px, 700 weight, -0.5px letter-spacing
- **Subtitle**: 14px, 400 weight
- **Section Label**: 16px, 600 weight, 0.3px letter-spacing
- **Button**: 14-15px, 600 weight, 0.3px letter-spacing
- **Body**: 13-14px, 400 weight
- **Monospace**: 13px, Consolas/Courier New

### Shadows
- **Card Shadow**: Blur 50px, Offset (0, 20px), Color `rgba(10, 14, 39, 0.78)`

## 🎯 Usage Guidelines

### Contrast Ratios
All text combinations meet WCAG AA standards:
- White text on dark backgrounds: 15:1+
- Primary buttons (white on cyan): 4.5:1+
- Error text on backgrounds: 4.5:1+

### Interactive States
1. **Default**: Base colors
2. **Hover**: Slightly lighter/darker (0891b2 for buttons, 475569 for borders)
3. **Pressed/Active**: Darker shade (0e7490)
4. **Focus**: Primary color border (#06b6d4)
5. **Disabled**: Muted gray tones

### Color Application
- **Backgrounds**: Use gradient for depth
- **Cards**: Semi-transparent with subtle borders
- **Primary Actions**: Vibrant cyan (#06b6d4)
- **Text**: High contrast whites and grays
- **Feedback**: Green for success, Rose for errors
- **Selection**: Cyan with low opacity

## 🔄 Consistency Rules
1. All auth pages (login/register) share identical styling
2. Home page uses same palette with glass-card variation
3. Buttons always use primary cyan (#06b6d4)
4. Error messages always use rose (#fb7185) with background tint
5. Success messages always use emerald (#10b981) with background tint
6. All borders use consistent thickness (1.5px for inputs)

## 🎨 Design Philosophy
- **Modern**: Clean, professional aesthetic
- **Depth**: Layered transparencies create visual hierarchy
- **Contrast**: High text contrast for readability
- **Consistency**: Unified color system across all pages
- **Accessibility**: WCAG AA compliant colors
- **Polish**: Smooth hover/focus transitions

