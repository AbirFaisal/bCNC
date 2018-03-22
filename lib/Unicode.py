#!/bin/env python
#
# Copyright and User License
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copyright Vasilis.Vlachoudis@cern.ch for the
# European Organization for Nuclear Research
#
# Please consult the documentation for the license
#
# DISCLAIMER
# ~~~~~~~~~~
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, IMPLIED WARRANTIES OF MERCHANTABILITY, OF
# SATISFACTORY QUALITY, AND FITNESS FOR A PARTICULAR PURPOSE
# OR USE ARE DISCLAIMED. THE COPYRIGHT HOLDERS AND THE
# AUTHORS MAKE NO REPRESENTATION THAT THE SOFTWARE AND
# MODIFICATIONS THEREOF, WILL NOT INFRINGE ANY PATENT,
# COPYRIGHT, TRADE SECRET OR OTHER PROPRIETARY RIGHT.
#
# LIMITATION OF LIABILITY
# ~~~~~~~~~~~~~~~~~~~~~~~
# THE COPYRIGHT HOLDERS AND THE AUTHORS SHALL HAVE NO
# LIABILITY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL,
# CONSEQUENTIAL, EXEMPLARY, OR PUNITIVE DAMAGES OF ANY
# CHARACTER INCLUDING, WITHOUT LIMITATION, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES, LOSS OF USE, DATA OR PROFITS,
# OR BUSINESS INTERRUPTION, HOWEVER CAUSED AND ON ANY THEORY
# OF CONTRACT, WARRANTY, TORT
# LIABILITY OR OTHERWISE, ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGES.
#
# Author:	Vasilis.Vlachoudis@cern.ch
# Date:	04-Sep-2014

# Greek characters http://en.wikipedia.org/wiki/List_of_Unicode_characters
GREEK_NUMERAL_SIGN = u"\u0374"
GREEK_LOWER_NUMERAL_SIGN = u"\u0375"
GREEK_YPOGEGRAMMENI = u"\u037A"
GREEK_SMALL_REVERSED_LUNATE_SIGMA_SYMBOL = u"\u037B"
GREEK_SMALL_DOTTED_LUNATE_SIGMA_SYMBOL = u"\u037C"
GREEK_SMALL_REVERSED_DOTTED_LUNATE_SIGMA_SYMBOL = u"\u037D"
GREEK_QUESTION_MARK = u"\u037E"
GREEK_ACUTE_ACCENT = u"\u0384"
GREEK_DIAERESIS_WITH_ACUTE_ACCENT = u"\u0385"
GREEK_CAPITAL_A_WITH_ACUTE_ACCENT = u"\u0386"
GREEK_ANO_TELEIA = u"\u0387"
GREEK_CAPITAL_EPSILON_WITH_ACUTE_ACCENT = u"\u0388"
GREEK_CAPITAL_ETA_WITH_ACUTE_ACCENT = u"\u0389"
GREEK_CAPITAL_IOTA_WITH_ACUTE_ACCENT = u"\u038A"
GREEK_CAPITAL_OMICRON_WITH_ACUTE_ACCENT = u"\u038C"
GREEK_CAPITAL_UPSILON_WITH_ACUTE_ACCENT = u"\u038E"
GREEK_CAPITAL_OMEGA_WITH_ACUTE_ACCENT = u"\u038F"
GREEK_SMALL_IOTA_WITH_DIAERESIS_AND_ACUTE_ACCENT = u"\u0390"
GREEK_CAPITAL_ALPHA = u"\u0391"
GREEK_CAPITAL_BETA = u"\u0392"
GREEK_CAPITAL_GAMMA = u"\u0393"
GREEK_CAPITAL_DELTA = u"\u0394"
GREEK_CAPITAL_EPSILON = u"\u0395"
GREEK_CAPITAL_ZETA = u"\u0396"
GREEK_CAPITAL_ETA = u"\u0397"
GREEK_CAPITAL_THETA = u"\u0398"
GREEK_CAPITAL_IOTA = u"\u0399"
GREEK_CAPITAL_KAPPA = u"\u039A"
GREEK_CAPITAL_LAMBDA = u"\u039B"
GREEK_CAPITAL_MU = u"\u039C"
GREEK_CAPITAL_NU = u"\u039D"
GREEK_CAPITAL_XI = u"\u039E"
GREEK_CAPITAL_OMICRON = u"\u039F"
GREEK_CAPITAL_PI = u"\u03A0"
GREEK_CAPITAL_RHO = u"\u03A1"
GREEK_CAPITAL_SIGMA = u"\u03A3"
GREEK_CAPITAL_TAU = u"\u03A4"
GREEK_CAPITAL_UPSILON = u"\u03A5"
GREEK_CAPITAL_PHI = u"\u03A6"
GREEK_CAPITAL_CHI = u"\u03A7"
GREEK_CAPITAL_PSI = u"\u03A8"
GREEK_CAPITAL_OMEGA = u"\u03A9"
GREEK_CAPITAL_IOTA_WITH_DIAERESIS = u"\u03AA"
GREEK_CAPITAL_UPSILON_WITH_DIAERESIS = u"\u03AB"
GREEK_SMALL_ALPHA_WITH_ACUTE_ACCENT = u"\u03AC"
GREEK_SMALL_EPSILON_WITH_ACUTE_ACCENT = u"\u03AD"
GREEK_SMALL_ETA_WITH_ACUTE_ACCENT = u"\u03AE"
GREEK_SMALL_IOTA_WITH_ACUTE_ACCENT = u"\u03AF"
GREEK_SMALL_UPSILON_WITH_DIAERESIS_AND_ACUTE_ACCENT = u"\u03B0"
GREEK_SMALL_ALPHA = u"\u03B1"
GREEK_SMALL_BETA = u"\u03B2"
GREEK_SMALL_GAMMA = u"\u03B3"
GREEK_SMALL_DELTA = u"\u03B4"
GREEK_SMALL_EPSILON = u"\u03B5"
GREEK_SMALL_ZETA = u"\u03B6"
GREEK_SMALL_ETA = u"\u03B7"
GREEK_SMALL_THETA = u"\u03B8"
GREEK_SMALL_IOTA = u"\u03B9"
GREEK_SMALL_KAPPA = u"\u03BA"
GREEK_SMALL_LAMBDA = u"\u03BB"
GREEK_SMALL_MU = u"\u03BC"
GREEK_SMALL_NU = u"\u03BD"
GREEK_SMALL_XI = u"\u03BE"
GREEK_SMALL_OMICRON = u"\u03BF"
GREEK_SMALL_PI = u"\u03C0"
GREEK_SMALL_RHO = u"\u03C1"
GREEK_SMALL_FINAL_SIGMA = u"\u03C2"
GREEK_SMALL_SIGMA = u"\u03C3"
GREEK_SMALL_TAU = u"\u03C4"
GREEK_SMALL_UPSILON = u"\u03C5"
GREEK_SMALL_PHI = u"\u03C6"
GREEK_SMALL_CHI = u"\u03C7"
GREEK_SMALL_PSI = u"\u03C8"
GREEK_SMALL_OMEGA = u"\u03C9"
GREEK_SMALL_IOTA_WITH_DIAERESIS = u"\u03CA"
GREEK_SMALL_UPSILON_WITH_DIAERESIS = u"\u03CB"
GREEK_SMALL_OMICRON_WITH_ACUTE_ACCENT = u"\u03CC"
GREEK_SMALL_UPSILON_WITH_ACUTE_ACCENT = u"\u03CD"
GREEK_SMALL_OMEGA_WITH_ACUTE_ACCENT = u"\u03CE"
GREEK_BETA_SYMBOL = u"\u03D0"
GREEK_THETA_SYMBOL = u"\u03D1"
GREEK_UPSILON_WITH_HOOK_SYMBOL = u"\u03D2"
GREEK_UPSILON_WITH_ACUTE_AND_HOOK_SYMBOL = u"\u03D3"
GREEK_UPSILON_WITH_DIAERESIS_AND_HOOK_SYMBOL = u"\u03D4"
GREEK_PHI_SYMBOL = u"\u03D5"
GREEK_PI_SYMBOL = u"\u03D6"
GREEK_KAI_SYMBOL = u"\u03D7"
GREEK_QOPPA = u"\u03D8"
GREEK_SMALL_QOPPA = u"\u03D9"
GREEK_STIGMA_LETTER = u"\u03DA"
GREEK_SMALL_STIGMA = u"\u03DB"
GREEK_DIGAMMA = u"\u03DC"
GREEK_SMALL_DIGAMMA = u"\u03DD"
GREEK_KOPPA = u"\u03DE"
GREEK_SMALL_KOPPA = u"\u03DF"
GREEK_SAMPI = u"\u03E0"
GREEK_SMALL_SAMPI = u"\u03E1"
COPTIC_CAPITAL_SHEI = u"\u03E2"
COPTIC_SMALL_SHEI = u"\u03E3"
COPTIC_CAPITAL_FEI = u"\u03E4"
COPTIC_SMALL_FEI = u"\u03E5"
COPTIC_CAPITAL_KHEI = u"\u03E6"
COPTIC_SMALL_KHEI = u"\u03E7"
COPTIC_CAPITAL_HORI = u"\u03E8"
COPTIC_SMALL_HORI = u"\u03E9"
COPTIC_CAPITAL_GANGIA = u"\u03EA"
COPTIC_SMALL_GANGIA = u"\u03EB"
COPTIC_CAPITAL_SHIMA = u"\u03EC"
COPTIC_SMALL_SHIMA = u"\u03ED"
COPTIC_CAPITAL_DEI = u"\u03EE"
COPTIC_SMALL_DEI = u"\u03EF"
GREEK_KAPPA_SYMBOL = u"\u03F0"
GREEK_RHO_SYMBOL = u"\u03F1"
GREEK_LUNATE_SIGMA_SYMBOL = u"\u03F2"
GREEK_YOT = u"\u03F3"
GREEK_CAPITAL_THETA_SYMBOL = u"\u03F4"
GREEK_LUNATE_EPSILON_SYMBOL = u"\u03F5"
GREEK_REVERSED_LUNATE_EPSILON_SYMBOL = u"\u03F6"
GREEK_CAPITAL_SHO = u"\u03F7"
GREEK_SMALL_SHO = u"\u03F8"
GREEK_CAPITAL_LUNATE_SIGMA_SYMBOL = u"\u03F9"
GREEK_CAPITAL_SAN = u"\u03FA"
GREEK_SMALL_SAN = u"\u03FB"
GREEK_RHO_WITH_STROKE_SYMBOL = u"\u03FC"
GREEK_CAPITAL_REVERSED_LUNATE_SIGMA_SYMBOL = u"\u03FD"
GREEK_CAPITAL_DOTTED_LUNATE_SIGMA_SYMBOL = u"\u03FE"
GREEK_CAPITAL_REVERSED_DOTTED_LUNATE_SIGMA_SYMBOL = u"\u03FF"

# Geometric Shapes http://en.wikipedia.org/wiki/Geometric_Shapes
BLACK_SQUARE = u"\u25A0"
WHITE_SQUARE = u"\u25A1"
WHITE_SQUARE_WITH_ROUNDED_CORNERS = u"\u25A2"
WHITE_SQUARE_CONTAINING_BLACK_SMALL_SQUARE = u"\u25A3"
SQUARE_WITH_HORIZONTAL_FILL = u"\u25A4"
SQUARE_WITH_VERTICAL_FILL = u"\u25A5"
SQUARE_WITH_ORTHOGONAL_CROSSHATCH_FILL = u"\u25A6"
SQUARE_WITH_UPPER_LEFT_TO_LOWER_RIGHT_FILL = u"\u25A7"
SQUARE_WITH_UPPER_RIGHT_TO_LOWER_LEFT_FILL = u"\u25A8"
SQUARE_WITH_DIAGONAL_CROSSHATCH_FILL = u"\u25A9"
BLACK_SMALL_SQUARE = u"\u25AA"
WHITE_SMALL_SQUARE = u"\u25AB"
BLACK_RECTANGLE = u"\u25AC"
WHITE_RECTANGLE = u"\u25AD"
BLACK_VERTICAL_RECTANGLE = u"\u25AE"
WHITE_VERTICAL_RECTANGLE = u"\u25AF"
BLACK_PARALLELOGRAM = u"\u25B0"
WHITE_PARALLELOGRAM = u"\u25B1"
BLACK_UP_POINTING_TRIANGLE = u"\u25B2"
WHITE_UP_POINTING_TRIANGLE = u"\u25B3"
BLACK_UP_POINTING_SMALL_TRIANGLE = u"\u25B4"
WHITE_UP_POINTING_SMALL_TRIANGLE = u"\u25B5"
BLACK_RIGHT_POINTING_TRIANGLE = u"\u25B6"
WHITE_RIGHT_POINTING_TRIANGLE = u"\u25B7"
BLACK_RIGHT_POINTING_SMALL_TRIANGLE = u"\u25B8"
WHITE_RIGHT_POINTING_SMALL_TRIANGLE = u"\u25B9"
BLACK_RIGHT_POINTING_POINTER = u"\u25BA"
WHITE_RIGHT_POINTING_POINTER = u"\u25BB"
BLACK_DOWN_POINTING_TRIANGLE = u"\u25BC"
WHITE_DOWN_POINTING_TRIANGLE = u"\u25BD"
BLACK_DOWN_POINTING_SMALL_TRIANGLE = u"\u25BE"
WHITE_DOWN_POINTING_SMALL_TRIANGLE = u"\u25BF"
BLACK_LEFT_POINTING_TRIANGLE = u"\u25C0"
WHITE_LEFT_POINTING_TRIANGLE = u"\u25C1"
BLACK_LEFT_POINTING_SMALL_TRIANGLE = u"\u25C2"
WHITE_LEFT_POINTING_SMALL_TRIANGLE = u"\u25C3"
BLACK_LEFT_POINTING_POINTER = u"\u25C4"
WHITE_LEFT_POINTING_POINTER = u"\u25C5"
BLACK_DIAMOND = u"\u25C6"
WHITE_DIAMOND = u"\u25C7"
WHITE_DIAMOND_CONTAINING_BLACK_SMALL_DIAMOND = u"\u25C8"
FISHEYE = u"\u25C9"
LOZENGE = u"\u25CA"
WHITE_CIRCLE = u"\u25CB"
DOTTED_CIRCLE = u"\u25CC"
CIRCLE_WITH_VERTICAL_FILL = u"\u25CD"
BULLSEYE = u"\u25CE"
BLACK_CIRCLE = u"\u25CF"
CIRCLE_WITH_LEFT_HALF_BLACK = u"\u25D0"
CIRCLE_WITH_RIGHT_HALF_BLACK = u"\u25D1"
CIRCLE_WITH_LOWER_HALF_BLACK = u"\u25D2"
CIRCLE_WITH_UPPER_HALF_BLACK = u"\u25D3"
CIRCLE_WITH_UPPER_RIGHT_QUADRANT_BLACK = u"\u25D4"
CIRCLE_WITH_ALL_BUT_UPPER_LEFT_QUADRANT_BLACK = u"\u25D5"
LEFT_HALF_BLACK_CIRCLE = u"\u25D6"
RIGHT_HALF_BLACK_CIRCLE = u"\u25D7"
INVERSE_BULLET = u"\u25D8"
INVERSE_WHITE_CIRCLE = u"\u25D9"
UPPER_HALF_INVERSE_WHITE_CIRCLE = u"\u25DA"
LOWER_HALF_INVERSE_WHITE_CIRCLE = u"\u25DB"
UPPER_LEFT_QUADRANT_CIRCULAR_ARC = u"\u25DC"
UPPER_RIGHT_QUADRANT_CIRCULAR_ARC = u"\u25DD"
LOWER_RIGHT_QUADRANT_CIRCULAR_ARC = u"\u25DE"
LOWER_LEFT_QUADRANT_CIRCULAR_ARC = u"\u25DF"
UPPER_HALF_CIRCLE = u"\u25E0"
LOWER_HALF_CIRCLE = u"\u25E1"
BLACK_LOWER_RIGHT_TRIANGLE = u"\u25E2"
BLACK_LOWER_LEFT_TRIANGLE = u"\u25E3"
BLACK_UPPER_LEFT_TRIANGLE = u"\u25E4"
BLACK_UPPER_RIGHT_TRIANGLE = u"\u25E5"
WHITE_BULLET = u"\u25E6"
SQUARE_WITH_LEFT_HALF_BLACK = u"\u25E7"
SQUARE_WITH_RIGHT_HALF_BLACK = u"\u25E8"
SQUARE_WITH_UPPER_LEFT_DIAGONAL_HALF_BLACK = u"\u25E9"
SQUARE_WITH_LOWER_RIGHT_DIAGONAL_HALF_BLACK = u"\u25EA"
WHITE_SQUARE_WITH_VERTICAL_BISECTING_LINE = u"\u25EB"
WHITE_UP_POINTING_TRIANGLE_WITH_DOT = u"\u25EC"
UP_POINTING_TRIANGLE_WITH_LEFT_HALF_BLACK = u"\u25ED"
UP_POINTING_TRIANGLE_WITH_RIGHT_HALF_BLACK = u"\u25EE"
LARGE_CIRCLE = u"\u25EF"
WHITE_SQUARE_WITH_UPPER_LEFT_QUADRANT = u"\u25F0"
WHITE_SQUARE_WITH_LOWER_LEFT_QUADRANT = u"\u25F1"
WHITE_SQUARE_WITH_LOWER_RIGHT_QUADRANT = u"\u25F2"
WHITE_SQUARE_WITH_UPPER_RIGHT_QUADRANT = u"\u25F3"
WHITE_CIRCLE_WITH_UPPER_LEFT_QUADRANT = u"\u25F4"
WHITE_CIRCLE_WITH_LOWER_LEFT_QUADRANT = u"\u25F5"
WHITE_CIRCLE_WITH_LOWER_RIGHT_QUADRANT = u"\u25F6"
WHITE_CIRCLE_WITH_UPPER_RIGHT_QUADRANT = u"\u25F7"
UPPER_LEFT_TRIANGLE = u"\u25F8"
UPPER_RIGHT_TRIANGLE = u"\u25F9"
LOWER_LEFT_TRIANGLE = u"\u25FA"
WHITE_MEDIUM_SQUARE = u"\u25FB"
BLACK_MEDIUM_SQUARE = u"\u25FC"
WHITE_MEDIUM_SMALL_SQUARE = u"\u25FD"
BLACK_MEDIUM_SMALL_SQUARE = u"\u25FE"
LOWER_RIGHT_TRIANGLE = u"\u25FF"

# Arrows (http://en.wikipedia.org/wiki/Arrow_%28symbol%29)
LEFTWARDS_ARROW = u"\u2190"
UPWARDS_ARROW = u"\u2191"
RIGHTWARDS_ARROW = u"\u2192"
DOWNWARDS_ARROW = u"\u2193"
LEFT_RIGHT_ARROW = u"\u2194"
UP_DOWN_ARROW = u"\u2195"
NORTH_WEST_ARROW = u"\u2196"
NORTH_EAST_ARROW = u"\u2197"
SOUTH_EAST_ARROW = u"\u2198"
SOUTH_WEST_ARROW = u"\u2199"
LEFTWARDS_ARROW_WITH_STROKE = u"\u219A"
RIGHTWARDS_ARROW_WITH_STROKE = u"\u219B"
LEFTWARDS_WAVE_ARROW = u"\u219C"
RIGHTWARDS_WAVE_ARROW = u"\u219D"
LEFTWARDS_TWO_HEADED_ARROW = u"\u219E"
UPWARDS_TWO_HEADED_ARROW = u"\u219F"
RIGHTWARDS_TWO_HEADED_ARROW = u"\u21A0"
DOWNWARDS_TWO_HEADED_ARROW = u"\u21A1"
LEFTWARDS_ARROW_WITH_TAIL = u"\u21A2"
RIGHTWARDS_ARROW_WITH_TAIL = u"\u21A3"
LEFTWARDS_ARROW_FROM_BAR = u"\u21A4"
UPWARDS_ARROW_FROM_BAR = u"\u21A5"
RIGHTWARDS_ARROW_FROM_BAR = u"\u21A6"
DOWNWARDS_ARROW_FROM_BAR = u"\u21A7"
UP_DOWN_ARROW_WITH_BASE = u"\u21A8"
LEFTWARDS_ARROW_WITH_HOOK = u"\u21A9"
RIGHTWARDS_ARROW_WITH_HOOK = u"\u21AA"
LEFTWARDS_ARROW_WITH_LOOP = u"\u21AB"
RIGHTWARDS_ARROW_WITH_LOOP = u"\u21AC"
LEFT_RIGHT_WAVE_ARROW = u"\u21AD"
LEFT_RIGHT_ARROW_WITH_STROKE = u"\u21AE"
DOWNWARDS_ZIGZAG_ARROW = u"\u21AF"
UPWARDS_ARROW_WITH_TIP_LEFTWARDS = u"\u21B0"
UPWARDS_ARROW_WITH_TIP_RIGHTWARDS = u"\u21B1"
DOWNWARDS_ARROW_WITH_TIP_LEFTWARDS = u"\u21B2"
DOWNWARDS_ARROW_WITH_TIP_RIGHTWARDS = u"\u21B3"
RIGHTWARDS_ARROW_WITH_CORNER_DOWNWARDS = u"\u21B4"
DOWNWARDS_ARROW_WITH_CORNER_LEFTWARDS = u"\u21B5"
ANTICLOCKWISE_TOP_SEMICIRCLE_ARROW = u"\u21B6"
CLOCKWISE_TOP_SEMICIRCLE_ARROW = u"\u21B7"
NORTH_WEST_ARROW_TO_LONG_BAR = u"\u21B8"
LEFTWARDS_ARROW_TO_BAR_OVER_RIGHTWARDS_ARROW_TO_BAR = u"\u21B9"
ANTICLOCKWISE_OPEN_CIRCLE_ARROW = u"\u21BA"
CLOCKWISE_OPEN_CIRCLE_ARROW = u"\u21BB"
LEFTWARDS_HARPOON_WITH_BARB_UPWARDS = u"\u21BC"
LEFTWARDS_HARPOON_WITH_BARB_DOWNWARDS = u"\u21BD"
UPWARDS_HARPOON_WITH_BARB_RIGHTWARDS = u"\u21BE"
UPWARDS_HARPOON_WITH_BARB_LEFTWARDS = u"\u21BF"
RIGHTWARDS_HARPOON_WITH_BARB_UPWARDS = u"\u21C0"
RIGHTWARDS_HARPOON_WITH_BARB_DOWNWARDS = u"\u21C1"
DOWNWARDS_HARPOON_WITH_BARB_RIGHTWARDS = u"\u21C2"
DOWNWARDS_HARPOON_WITH_BARB_LEFTWARDS = u"\u21C3"
RIGHTWARDS_ARROW_OVER_LEFTWARDS_ARROW = u"\u21C4"
UPWARDS_ARROW_LEFTWARDS_OF_DOWNWARDS_ARROW = u"\u21C5"
LEFTWARDS_ARROW_OVER_RIGHTWARDS_ARROW = u"\u21C6"
LEFTWARDS_PAIRED_ARROWS = u"\u21C7"
UPWARDS_PAIRED_ARROWS = u"\u21C8"
RIGHTWARDS_PAIRED_ARROWS = u"\u21C9"
DOWNWARDS_PAIRED_ARROWS = u"\u21CA"
LEFTWARDS_HARPOON_OVER_RIGHTWARDS_HARPOON = u"\u21CB"
RIGHTWARDS_HARPOON_OVER_LEFTWARDS_HARPOON = u"\u21CC"
LEFTWARDS_DOUBLE_ARROW_WITH_STROKE = u"\u21CD"
LEFT_RIGHT_DOUBLE_ARROW_WITH_STROKE = u"\u21CE"
RIGHTWARDS_DOUBLE_ARROW_WITH_STROKE = u"\u21CF"
LEFTWARDS_DOUBLE_ARROW = u"\u21D0"
UPWARDS_DOUBLE_ARROW = u"\u21D1"
RIGHTWARDS_DOUBLE_ARROW = u"\u21D2"
DOWNWARDS_DOUBLE_ARROW = u"\u21D3"
LEFT_RIGHT_DOUBLE_ARROW = u"\u21D4"
UP_DOWN_DOUBLE_ARROW = u"\u21D5"
NORTH_WEST_DOUBLE_ARROW = u"\u21D6"
NORTH_EAST_DOUBLE_ARROW = u"\u21D7"
SOUTH_EAST_DOUBLE_ARROW = u"\u21D8"
SOUTH_WEST_DOUBLE_ARROW = u"\u21D9"
LEFTWARDS_TRIPLE_ARROW = u"\u21DA"
RIGHTWARDS_TRIPLE_ARROW = u"\u21DB"
LEFTWARDS_SQUIGGLE_ARROW = u"\u21DC"
RIGHTWARDS_SQUIGGLE_ARROW = u"\u21DD"
UPWARDS_ARROW_WITH_DOUBLE_STROKE = u"\u21DE"
DOWNWARDS_ARROW_WITH_DOUBLE_STROKE = u"\u21DF"
LEFTWARDS_DASHED_ARROW = u"\u21E0"
UPWARDS_DASHED_ARROW = u"\u21E1"
RIGHTWARDS_DASHED_ARROW = u"\u21E2"
DOWNWARDS_DASHED_ARROW = u"\u21E3"
LEFTWARDS_ARROW_TO_BAR = u"\u21E4"
RIGHTWARDS_ARROW_TO_BAR = u"\u21E5"
LEFTWARDS_THICK_ARROW = u"\u21E6"
UPWARDS_THICK_ARROW = u"\u21E7"
RIGHTWARDS_THICK_ARROW = u"\u21E8"
DOWNWARDS_THICK_ARROW = u"\u21E9"
UPWARDS_THICK_ARROW_FROM_BAR = u"\u21EA"
UPWARDS_THICK_ARROW_ON_PEDESTAL = u"\u21EB"
UPWARDS_THICK_ARROW_ON_PEDESTAL_WITH_HORIZONTAL_BAR = u"\u21EC"
UPWARDS_THICK_ARROW_ON_PEDESTAL_WITH_VERTICAL_BAR = u"\u21ED"
UPWARDS_THICK_DOUBLE_ARROW = u"\u21EE"
UPWARDS_THICK_DOUBLE_ARROW_ON_PEDESTAL = u"\u21EF"
RIGHTWARDS_THICK_ARROW_FROM_WALL = u"\u21F0"
NORTH_WEST_ARROW_TO_CORNER = u"\u21F1"
SOUTH_EAST_ARROW_TO_CORNER = u"\u21F2"
UP_DOWN_THICK_ARROW = u"\u21F3"
RIGHT_ARROW_WITH_SMALL_CIRCLE = u"\u21F4"
DOWNWARDS_ARROW_LEFTWARDS_OF_UPWARDS_ARROW = u"\u21F5"
THREE_RIGHTWARDS_ARROWS = u"\u21F6"
LEFTWARDS_ARROW_WITH_VERTICAL_STROKE = u"\u21F7"
RIGHTWARDS_ARROW_WITH_VERTICAL_STROKE = u"\u21F8"
LEFT_RIGHT_ARROW_WITH_VERTICAL_STROKE = u"\u21F9"
LEFTWARDS_ARROW_WITH_DOUBLE_VERTICAL_STROKE = u"\u21FA"
RIGHTWARDS_ARROW_WITH_DOUBLE_VERTICAL_STROKE = u"\u21FB"
LEFT_RIGHT_ARROW_WITH_DOUBLE_VERTICAL_STROKE = u"\u21FC"
LEFTWARDS_OPEN_HEADED_ARROW = u"\u21FD"
RIGHTWARDS_OPEN_HEADED_ARROW = u"\u21FE"
LEFT_RIGHT_OPEN_HEADED_ARROW = u"\u21FF"

# Miscellaneous Symbols
BLACK_SUN_WITH_RAYS = u"\u2600"
CLOUD = u"\u2601"
UMBRELLA = u"\u2602"
SNOWMAN = u"\u2603"
COMET = u"\u2604"
BLACK_STAR = u"\u2605"
STAR = u"\u2606"
LIGHTNING = u"\u2607"
THUNDERSTORM = u"\u2608"
SUN = u"\u2609"
ASCENDING_NODE = u"\u260A"
DESCENDING_NODE = u"\u260B"
CONJUNCTION = u"\u260C"
OPPOSITION = u"\u260D"
BLACK_TELEPHONE = u"\u260E"
WHITE_TELEPHONE = u"\u260F"
BALLOT_BOX = u"\u2610"
BALLOT_BOX_WITH_CHECK = u"\u2611"
BALLOT_BOX_WITH_X = u"\u2612"
SALTIRE = u"\u2613"
UMBRELLA_WITH_RAINDROPS = u"\u2614"
HOT_BEVERAGE = u"\u2615"
WHITE_SHOGI_PIECE = u"\u2616"
BLACK_SHOGI_PIECE = u"\u2617"
SHAMROCK = u"\u2618"
REVERSED_ROTATED_FLORAL_HEART_BULLET = u"\u2619"
BLACK_LEFT_POINTING_INDEX = u"\u261A"
BLACK_RIGHT_POINTING_INDEX = u"\u261B"
WHITE_LEFT_POINTING_INDEX = u"\u261C"
WHITE_UP_POINTING_INDEX = u"\u261D"
WHITE_RIGHT_POINTING_INDEX = u"\u261E"
WHITE_DOWN_POINTING_INDEX = u"\u261F"
SKULL_AND_CROSSBONES = u"\u2620"
CAUTION_SIGN = u"\u2621"
RADIOACTIVE_SIGN = u"\u2622"
BIOHAZARD_SIGN = u"\u2623"
CADUCEUS = u"\u2624"
ANKH = u"\u2625"
RUSSIAN_CROSS = u"\u2626"
CHI_RHO = u"\u2627"
CROSS_OF_LORRAINE = u"\u2628"
CROSS_OF_JERUSALEM = u"\u2629"
STAR_AND_CRESCENT = u"\u262A"
FARSI_SYMBOL = u"\u262B"
ADI_SHAKTI = u"\u262C"
HAMMER_AND_SICKLE = u"\u262D"
PEACE_SYMBOL = u"\u262E"
YIN_AND_YANG = u"\u262F"
TRIGRAM_FOR_HEAVEN = u"\u2630"
TRIGRAM_FOR_LAKE = u"\u2631"
TRIGRAM_FOR_FIRE = u"\u2632"
TRIGRAM_FOR_THUNDER = u"\u2633"
TRIGRAM_FOR_WIND = u"\u2634"
TRIGRAM_FOR_WATER = u"\u2635"
TRIGRAM_FOR_MOUNTAIN = u"\u2636"
TRIGRAM_FOR_EARTH = u"\u2637"
WHEEL_OF_DHARMA = u"\u2638"
WHITE_FROWNING_FACE = u"\u2639"
WHITE_SMILING_FACE = u"\u263A"
BLACK_SMILING_FACE = u"\u263B"
WHITE_SUN_WITH_RAYS = u"\u263C"
FIRST_QUARTER_MOON = u"\u263D"
LAST_QUARTER_MOON = u"\u263E"
MERCURY = u"\u263F"
FEMALE_SIGN = u"\u2640"
EARTH = u"\u2641"
MALE_SIGN = u"\u2642"
JUPITER = u"\u2643"
SATURN = u"\u2644"
URANUS = u"\u2645"
NEPTUNE = u"\u2646"
PLUTO = u"\u2647"
ARIES = u"\u2648"
TAURUS = u"\u2649"
GEMINI = u"\u264A"
CANCER = u"\u264B"
LEO = u"\u264C"
VIRGO = u"\u264D"
LIBRA = u"\u264E"
SCORPIUS = u"\u264F"
SAGITTARIUS = u"\u2650"
CAPRICORN = u"\u2651"
AQUARIUS = u"\u2652"
PISCES = u"\u2653"
WHITE_CHESS_KING = u"\u2654"
WHITE_CHESS_QUEEN = u"\u2655"
WHITE_CHESS_ROOK = u"\u2656"
WHITE_CHESS_BISHOP = u"\u2657"
WHITE_CHESS_KNIGHT = u"\u2658"
WHITE_CHESS_PAWN = u"\u2659"
BLACK_CHESS_KING = u"\u265A"
BLACK_CHESS_QUEEN = u"\u265B"
BLACK_CHESS_ROOK = u"\u265C"
BLACK_CHESS_BISHOP = u"\u265D"
BLACK_CHESS_KNIGHT = u"\u265E"
BLACK_CHESS_PAWN = u"\u265F"
BLACK_SPADE_SUIT = u"\u2660"
WHITE_HEART_SUIT = u"\u2661"
WHITE_DIAMOND_SUIT = u"\u2662"
BLACK_CLUB_SUIT = u"\u2663"
WHITE_SPADE_SUIT = u"\u2664"
BLACK_HEART_SUIT = u"\u2665"
BLACK_DIAMOND_SUIT = u"\u2666"
WHITE_CLUB_SUIT = u"\u2667"
HOT_SPRING = u"\u2668"
QUARTER_NOTE = u"\u2669"
EIGHTH_NOTE = u"\u266A"
BEAMED_EIGHTH_NOTES = u"\u266B"
BEAMED_SIXTEENTH_NOTES = u"\u266C"
MUSIC_FLAT_SIGN = u"\u266D"
MUSIC_NATURAL_SIGN = u"\u266E"
MUSIC_SHARP_SIGN = u"\u266F"
WEST_SYRIAC_CROSS = u"\u2670"
EAST_SYRIAC_CROSS = u"\u2671"
UNIVERSAL_RECYCLING_SYMBOL = u"\u2672"
RECYCLING_SYMBOL_FOR_TYPE_1_PLASTICS = u"\u2673"
RECYCLING_SYMBOL_FOR_TYPE_2_PLASTICS = u"\u2674"
RECYCLING_SYMBOL_FOR_TYPE_3_PLASTICS = u"\u2675"
RECYCLING_SYMBOL_FOR_TYPE_4_PLASTICS = u"\u2676"
RECYCLING_SYMBOL_FOR_TYPE_5_PLASTICS = u"\u2677"
RECYCLING_SYMBOL_FOR_TYPE_6_PLASTICS = u"\u2678"
RECYCLING_SYMBOL_FOR_TYPE_7_PLASTICS = u"\u2679"
RECYCLING_SYMBOL_FOR_GENERIC_MATERIALS = u"\u267A"
BLACK_UNIVERSAL_RECYCLING_SYMBOL = u"\u267B"
RECYCLED_PAPER_SYMBOL = u"\u267C"
PARTIALLY_RECYCLED_PAPER_SYMBOL = u"\u267D"
PERMANENT_PAPER_SIGN = u"\u267E"
WHEELCHAIR_SYMBOL = u"\u267F"
DIE_FACE_1 = u"\u2680"
DIE_FACE_2 = u"\u2681"
DIE_FACE_3 = u"\u2682"
DIE_FACE_4 = u"\u2683"
DIE_FACE_5 = u"\u2684"
DIE_FACE_6 = u"\u2685"
WHITE_CIRCLE_WITH_DOT_RIGHT = u"\u2686"
WHITE_CIRCLE_WITH_TWO_DOTS = u"\u2687"
BLACK_CIRCLE_WITH_WHITE_DOT_RIGHT = u"\u2688"
BLACK_CIRCLE_WITH_TWO_WHITE_DOTS = u"\u2689"
MONOGRAM_FOR_YANG = u"\u268A"
MONOGRAM_FOR_YIN = u"\u268B"
DIGRAM_FOR_GREATER_YANG = u"\u268C"
DIGRAM_FOR_LESSER_YIN = u"\u268D"
DIGRAM_FOR_LESSER_YANG = u"\u268E"
DIGRAM_FOR_GREATER_YIN = u"\u268F"
WHITE_FLAG = u"\u2690"
BLACK_FLAG = u"\u2691"
HAMMER_AND_PICK = u"\u2692"
ANCHOR = u"\u2693"
CROSSED_SWORDS = u"\u2694"
STAFF_OF_AESCULAPIUS = u"\u2695"
WEIGHING_SCALES = u"\u2696"
ALEMBIC = u"\u2697"
FLOWER = u"\u2698"
GEAR = u"\u2699"
STAFF_OF_HERMES = u"\u269A"
ATOM_SYMBOL = u"\u269B"
FLEUR_DE_LIS = u"\u269C"
OUTLINED_WHITE_STAR = u"\u269D"
THREE_LINES_CONVERGING_RIGHT = u"\u269E"
THREE_LINES_CONVERGING_LEFT = u"\u269F"
WARNING_SIGN = u"\u26A0"
HIGH_VOLTAGE_SIGN = u"\u26A1"
DOUBLED_FEMALE_SIGN = u"\u26A2"
DOUBLED_MALE_SIGN = u"\u26A3"
INTERLOCKED_MALE_AND_FEMALE_SIGN = u"\u26A4"
MALE_AND_FEMALE_SIGN = u"\u26A5"
MALE_WITH_STROKE_SIGN = u"\u26A6"
MALE_WITH_STROKE_AND_MALE_AND_FEMALE_SIGN = u"\u26A7"
VERTICAL_MALE_WITH_STROKE_SIGN = u"\u26A8"
HORIZONTAL_MALE_WITH_STROKE_SIGN = u"\u26A9"
MEDIUM_WHITE_CIRCLE = u"\u26AA"
MEDIUM_BLACK_CIRCLE = u"\u26AB"
MEDIUM_SMALL_WHITE_CIRCLE = u"\u26AC"
MARRIAGE_SYMBOL = u"\u26AD"
DIVORCE_SYMBOL = u"\u26AE"
UNMARRIED_PARTNERSHIP_SYMBOL = u"\u26AF"
COFFIN = u"\u26B0"
FUNERAL_URN = u"\u26B1"
NEUTER = u"\u26B2"
CERES = u"\u26B3"
PALLAS = u"\u26B4"
JUNO = u"\u26B5"
VESTA = u"\u26B6"
CHIRON = u"\u26B7"
BLACK_MOON_LILITH = u"\u26B8"
SEXTILE = u"\u26B9"
SEMISEXTILE = u"\u26BA"
QUINCUNX = u"\u26BB"
SESQUIQUADRATE = u"\u26BC"
SOCCER_BALL = u"\u26BD"
BASEBALL = u"\u26BE"
SQUARED_KEY = u"\u26BF"
WHITE_DRAUGHTS_MAN = u"\u26C0"
WHITE_DRAUGHTS_KING = u"\u26C1"
BLACK_DRAUGHTS_MAN = u"\u26C2"
BLACK_DRAUGHTS_KING = u"\u26C3"
SNOWMAN_WITHOUT_SNOW = u"\u26C4"
SUN_BEHIND_CLOUD = u"\u26C5"
RAIN = u"\u26C6"
BLACK_SNOWMAN = u"\u26C7"
THUNDER_CLOUD_AND_RAIN = u"\u26C8"
TURNED_WHITE_SHOGI_PIECE = u"\u26C9"
TURNED_BLACK_SHOGI_PIECE = u"\u26CA"
WHITE_DIAMOND_IN_SQUARE = u"\u26CB"
CROSSING_LANES = u"\u26CC"
DISABLED_CAR = u"\u26CD"
OPHIUCHUS = u"\u26CE"
PICK = u"\u26CF"
CAR_SLIDING = u"\u26D0"
HELMET_WITH_WHITE_CROSS = u"\u26D1"
CIRCLED_CROSSING_LANES = u"\u26D2"
CHAINS = u"\u26D3"
NO_ENTRY = u"\u26D4"
ALTERNATE_ONE_WAY_LEFT_WAY_TRAFFIC = u"\u26D5"
BLACK_TWO_WAY_LEFT_WAY_TRAFFIC = u"\u26D6"
WHITE_TWO_WAY_LEFT_WAY_TRAFFIC = u"\u26D7"
BLACK_LEFT_LANE_MERGE = u"\u26D8"
WHITE_LEFT_LANE_MERGE = u"\u26D9"
DRIVE_SLOW_SIGN = u"\u26DA"
HEAVY_WHITE_DOWN_POINTING_TRIANGLE = u"\u26DB"
LEFT_CLOSED_ENTRY = u"\u26DC"
SQUARED_SALTIRE = u"\u26DD"
FALLING_DIAGONAL_IN_WHITE_CIRCLE_IN_BLACK_SQUARE = u"\u26DE"
BLACK_TRUCK = u"\u26DF"
RESTRICTED_LEFT_ENTRY_1 = u"\u26E0"
RESTRICTED_LEFT_ENTRY_2 = u"\u26E1"
ASTRONOMICAL_SYMBOL_FOR_URANUS = u"\u26E2"
HEAVY_CIRCLE_WITH_STROKE_AND_TWO_DOTS_ABOVE = u"\u26E3"
PENTAGRAM = u"\u26E4"
RIGHT_HANDED_INTERLACED_PENTAGRAM = u"\u26E5"
LEFT_HANDED_INTERLACED_PENTAGRAM = u"\u26E6"
INVERTED_PENTAGRAM = u"\u26E7"
BLACK_CROSS_ON_SHIELD = u"\u26E8"
SHINTO_SHRINE = u"\u26E9"
CHURCH = u"\u26EA"
CASTLE = u"\u26EB"
HISTORIC_SITE = u"\u26EC"
GEAR_WITHOUT_HUB = u"\u26ED"
GEAR_WITH_HANDLES = u"\u26EE"
MAP_SYMBOL_FOR_LIGHTHOUSE = u"\u26EF"
MOUNTAIN = u"\u26F0"
UMBRELLA_ON_GROUND = u"\u26F1"
FOUNTAIN = u"\u26F2"
FLAG_IN_HOLE = u"\u26F3"
FERRY = u"\u26F4"
SAILBOAT = u"\u26F5"
SQUARE_FOUR_CORNERS = u"\u26F6"
SKIER = u"\u26F7"
ICE_SKATE = u"\u26F8"
PERSON_WITH_BALL = u"\u26F9"
TENT = u"\u26FA"
JAPANESE_BANK_SYMBOL = u"\u26FB"
HEADSTONE_GRAVEYARD_SYMBOL = u"\u26FC"
FUEL_PUMP = u"\u26FD"
CUP_ON_BLACK_SQUARE = u"\u26FE"
WHITE_FLAG_WITH_HORIZONTAL_MIDDLE_BLACK_STRIPE = u"\u26FF"

# Mathematical symbols
MATH_TIMES = u"\u00D7"
MATH_HEAVY_MULTIPLICATION = u"\u2716"
MATH_OSLASH = u"\u00D8"
MATH_UP_TACK = u"\u22A5"
