# Visual Analysis First Rule

## The Rule

**You MUST visually analyze hero reference images BEFORE writing any prompt.** Do NOT rely solely on the text in Section A of PRODUCT_SHOT_SKILL.md.

## Why

Section A gives you numbers: hex codes, f-stops, degrees, ratios. But it does NOT give you:
- The actual warmth of the light
- How shadows feel (soft? feathered? dramatic?)
- The breathing room in the composition
- The premium/luxury atmosphere
- The way the product sits in the space
- The texture of the background

Vision gives you the SOUL of the style. Numbers give you the skeleton.

## Workflow

1. **Load hero reference images** with vision_analyze (or delegate_task with vision)
2. **Observe** what you SEE, not what Section A says:
   - Actual lighting feel (warm? clinical? dramatic?)
   - Background texture and gradient feel
   - Product positioning and scale
   - Shadow quality (hard/soft/warm/cool)
   - Overall mood and atmosphere
3. **Write down observations** — this is your visual anchor
4. **Then write the prompt** informed by BOTH the visual analysis AND Section A

## If No Vision Available

Say so IMMEDIATELY. Ask the user to describe what they see in the reference images. Do NOT guess or fabricate visual observations.

## Example

**Section A says:** "key light upper-left at 45°, 3200-3800K warm golden"
**Vision says:** "The light wraps the product like golden hour sunshine, creating a soft glow that makes the glass bottle look precious and warm"

The prompt should use the VISION observation, not the Section A number. The number is for verification; the vision is for creation.