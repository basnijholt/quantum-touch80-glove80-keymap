# Updated existing behaviors
existing_behaviors = {
    "bspc_del": {
        "compatible": "zmk,behavior-mod-morph",
        "bindings": ["&kp BACKSPACE", "&kp DELETE"],
        "mods": "<(MOD_LSFT|MOD_RSFT)>",
        "keep-mods": "<0>"
    },
    "td_caps_lshift": {
        "compatible": "zmk,behavior-tap-dance",
        "tapping-term-ms": "<200>",
        "bindings": ["&kp LSHIFT", "&caps_word"]
    },
    "td_caps_rshift": {
        "compatible": "zmk,behavior-tap-dance",
        "tapping-term-ms": "<200>",
        "bindings": ["&kp RSHIFT", "&caps_word"]
    },
    "td_lgui_enter": {
        "compatible": "zmk,behavior-tap-dance",
        "tapping-term-ms": "<200>",
        "bindings": ["&kp LGUI", "&kp ENTER"]
    },
    "behavior_caps_word": {
        "continue-list": [
            "UNDERSCORE",
            "BACKSPACE", "DELETE",
            "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8", "N9", "N0"
        ]
    }
}

# Define the new keys for mod-tap behaviors
new_keys = [
    ('N1', 'EXCL'),
    ('N2', 'AT'),
    ('N3', 'HASH'),
    ('N4', 'DLR'),
    ('N5', 'PERC'),
    ('N6', 'CIRC'),
    ('N7', 'AMPR'),
    ('N8', 'ASTER'),
    ('N9', 'LPRN'),
    ('N0', 'RPRN'),
    ('MINUS', 'UNDERSCORE'),
    ('EQL', 'PLUS'),
    ('LBKT', 'LCBR'),
    ('RBKT', 'RCBR'),
    ('SCOLON', 'COLON'),
    ('QUOTE', 'DQUO'),
    ('COMMA', 'LT'),
    ('DOT', 'GT'),
    ('SLASH', 'QMARK'),
    ('BSPC', 'PIPE'),
    ('GRAVE', 'TILDE')
]

# Generate the configuration script
def generate_config_script(existing_behaviors, new_keys):
    config_script = "behaviors {\n"
    for behavior, details in existing_behaviors.items():
        config_script += f"    {behavior}: {behavior.replace('_', ' ')} {{\n"
        for key, value in details.items():
            if isinstance(value, list):
                config_script += f"        {key} = <" + ", ".join(value) + ">;\n"
            else:
                config_script += f"        {key} = {value};\n"
        config_script += "    };\n"
    
    for tap_key, hold_key in new_keys:
        behavior_name = f"mt_{tap_key.lower()}_{hold_key.lower()}"
        config_script += f"    {behavior_name}: mod_tap_{tap_key.lower()}_{hold_key.lower()} {{\n"
        config_script += "        compatible = \"zmk,behavior-mod-tap\";\n"
        config_script += f"        label = \"{tap_key} / {hold_key}\";\n"
        config_script += "        tapping-term-ms = <200>;\n"
        config_script += "        mod = <MOD_LSFT>;\n"
        config_script += f"        tap = <{tap_key}>;\n"
        config_script += f"        hold = <{hold_key}>;\n"
        config_script += "    };\n"

    config_script += "};"
    return config_script

# Generate and print the configuration script
config_script = generate_config_script(existing_behaviors, new_keys)
print(config_script)

