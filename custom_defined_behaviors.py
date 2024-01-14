# Jinja2 template for generating ZMK configuration

from jinja2 import Template

# Template for the behaviors configuration
template_string = """
behaviors {
    bspc_del: backspace_delete {
        compatible = "zmk,behavior-mod-morph";
        #binding-cells = <0>;
        bindings = <&kp BACKSPACE>, <&kp DELETE>;
        mods = <(MOD_LSFT|MOD_RSFT)>;
        keep-mods = <0>;
    };
    td_caps_lshift: tap_dance_caps_lshift {
        compatible = "zmk,behavior-tap-dance";
        #binding-cells = <0>;
        tapping-term-ms = <200>;
        bindings = <&kp LSHIFT>, <&caps_word>;
    };
    td_caps_rshift: tap_dance_caps_rshift {
        compatible = "zmk,behavior-tap-dance";
        #binding-cells = <0>;
        tapping-term-ms = <200>;
        bindings = <&kp RSHIFT>, <&caps_word>;
    };
    td_lgui_enter: tap_dance_lgui_enter {
        compatible = "zmk,behavior-tap-dance";
        #binding-cells = <0>;
        tapping-term-ms = <200>;
        bindings = <&kp LGUI>, <&kp ENTER>;
    };
    behavior_caps_word {
        continue-list = <
            UNDERSCORE
            BACKSPACE DELETE
            N1 N2 N3 N4 N5 N6 N7 N8 N9 N0
        >;
    };
    {% for tap_key, hold_key in keys %}
    mt_{{ tap_key|lower }}_{{ hold_key|lower }}: mod_tap_{{ tap_key|lower }}_{{ hold_key|lower }} {
        compatible = "zmk,behavior-mod-tap";
        #binding-cells = <0>;
        label = "{{ tap_key }} / {{ hold_key }}";
        tapping-term-ms = <200>;
        mod = <MOD_LSFT>;
        tap = <{{ tap_key }}>;
        hold = <{{ hold_key }}>;
    };
    {% endfor %}
};
"""

# Define the new keys for mod-tap behaviors
keys = [
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

# Render the template with the keys
template = Template(template_string)
config_script = template.render(keys=keys)

print(config_script)

