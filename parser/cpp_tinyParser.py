# Generated from ./parser/cpp_tiny.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,62,450,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,5,0,72,8,0,10,0,12,0,75,9,0,1,1,1,1,1,1,1,1,1,1,
        3,1,82,8,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,90,8,1,1,1,3,1,93,8,1,1,2,
        1,2,3,2,97,8,2,1,3,1,3,1,3,3,3,102,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,3,6,114,8,6,1,6,3,6,117,8,6,1,6,1,6,1,6,3,6,122,8,
        6,1,6,3,6,125,8,6,1,6,5,6,128,8,6,10,6,12,6,131,9,6,3,6,133,8,6,
        1,6,1,6,1,6,1,7,1,7,1,7,3,7,141,8,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,9,3,9,151,8,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,159,8,10,1,10,1,
        10,1,10,3,10,164,8,10,1,10,5,10,167,8,10,10,10,12,10,170,9,10,3,
        10,172,8,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,183,
        8,11,10,11,12,11,186,9,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,
        208,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,5,14,239,8,14,10,14,12,14,242,9,14,1,15,
        1,15,5,15,246,8,15,10,15,12,15,249,9,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,3,16,270,8,16,1,16,1,16,1,16,3,16,275,8,16,3,16,277,8,16,1,
        16,1,16,1,16,1,16,1,16,1,16,3,16,285,8,16,1,16,1,16,1,16,1,16,3,
        16,291,8,16,1,16,1,16,3,16,295,8,16,1,16,1,16,1,16,3,16,300,8,16,
        1,16,1,16,1,16,1,16,3,16,306,8,16,1,17,1,17,1,18,1,18,1,18,1,18,
        3,18,314,8,18,1,19,1,19,3,19,318,8,19,1,20,1,20,1,20,1,20,1,20,3,
        20,325,8,20,1,21,1,21,3,21,329,8,21,1,21,1,21,1,21,1,21,5,21,335,
        8,21,10,21,12,21,338,9,21,3,21,340,8,21,1,21,1,21,1,22,1,22,3,22,
        346,8,22,1,23,1,23,1,24,1,24,1,24,3,24,353,8,24,1,24,1,24,1,25,1,
        25,1,26,1,26,1,26,3,26,362,8,26,1,26,1,26,1,26,5,26,367,8,26,10,
        26,12,26,370,9,26,1,26,3,26,373,8,26,1,26,1,26,3,26,377,8,26,1,27,
        1,27,1,28,1,28,1,28,3,28,384,8,28,1,28,4,28,387,8,28,11,28,12,28,
        388,1,29,1,29,1,29,1,29,5,29,395,8,29,10,29,12,29,398,9,29,3,29,
        400,8,29,1,29,1,29,3,29,404,8,29,1,30,1,30,1,30,1,30,1,30,1,30,3,
        30,412,8,30,1,31,1,31,1,31,3,31,417,8,31,1,31,1,31,1,31,5,31,422,
        8,31,10,31,12,31,425,9,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,5,32,436,8,32,10,32,12,32,439,9,32,3,32,441,8,32,1,32,3,32,
        444,8,32,3,32,446,8,32,1,33,1,33,1,33,0,1,28,34,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,0,12,1,0,31,33,1,0,42,43,1,0,38,39,1,0,40,41,2,0,
        47,50,52,52,1,0,53,54,1,0,45,46,1,0,58,59,2,0,44,44,56,56,2,0,1,
        1,7,12,1,0,2,6,2,0,40,40,45,45,499,0,73,1,0,0,0,2,92,1,0,0,0,4,96,
        1,0,0,0,6,101,1,0,0,0,8,103,1,0,0,0,10,106,1,0,0,0,12,109,1,0,0,
        0,14,140,1,0,0,0,16,142,1,0,0,0,18,145,1,0,0,0,20,154,1,0,0,0,22,
        176,1,0,0,0,24,189,1,0,0,0,26,192,1,0,0,0,28,207,1,0,0,0,30,243,
        1,0,0,0,32,305,1,0,0,0,34,307,1,0,0,0,36,313,1,0,0,0,38,317,1,0,
        0,0,40,319,1,0,0,0,42,328,1,0,0,0,44,345,1,0,0,0,46,347,1,0,0,0,
        48,349,1,0,0,0,50,356,1,0,0,0,52,361,1,0,0,0,54,378,1,0,0,0,56,380,
        1,0,0,0,58,403,1,0,0,0,60,405,1,0,0,0,62,416,1,0,0,0,64,445,1,0,
        0,0,66,447,1,0,0,0,68,72,3,2,1,0,69,72,3,4,2,0,70,72,3,22,11,0,71,
        68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,
        0,73,74,1,0,0,0,74,1,1,0,0,0,75,73,1,0,0,0,76,77,5,19,0,0,77,78,
        5,47,0,0,78,81,5,1,0,0,79,80,5,28,0,0,80,82,5,1,0,0,81,79,1,0,0,
        0,81,82,1,0,0,0,82,83,1,0,0,0,83,93,5,48,0,0,84,85,5,19,0,0,85,86,
        5,26,0,0,86,89,5,1,0,0,87,88,5,28,0,0,88,90,5,1,0,0,89,87,1,0,0,
        0,89,90,1,0,0,0,90,91,1,0,0,0,91,93,5,26,0,0,92,76,1,0,0,0,92,84,
        1,0,0,0,93,3,1,0,0,0,94,97,3,6,3,0,95,97,3,14,7,0,96,94,1,0,0,0,
        96,95,1,0,0,0,97,5,1,0,0,0,98,102,3,8,4,0,99,102,3,10,5,0,100,102,
        3,12,6,0,101,98,1,0,0,0,101,99,1,0,0,0,101,100,1,0,0,0,102,7,1,0,
        0,0,103,104,5,29,0,0,104,105,3,10,5,0,105,9,1,0,0,0,106,107,3,26,
        13,0,107,108,5,36,0,0,108,11,1,0,0,0,109,110,3,44,22,0,110,111,3,
        62,31,0,111,132,5,20,0,0,112,114,5,29,0,0,113,112,1,0,0,0,113,114,
        1,0,0,0,114,116,1,0,0,0,115,117,5,45,0,0,116,115,1,0,0,0,116,117,
        1,0,0,0,117,118,1,0,0,0,118,129,3,26,13,0,119,121,5,27,0,0,120,122,
        5,29,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,125,
        5,45,0,0,124,123,1,0,0,0,124,125,1,0,0,0,125,126,1,0,0,0,126,128,
        3,26,13,0,127,119,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,
        1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,132,113,1,0,0,0,132,133,
        1,0,0,0,133,134,1,0,0,0,134,135,5,21,0,0,135,136,5,36,0,0,136,13,
        1,0,0,0,137,141,3,16,8,0,138,141,3,18,9,0,139,141,3,20,10,0,140,
        137,1,0,0,0,140,138,1,0,0,0,140,139,1,0,0,0,141,15,1,0,0,0,142,143,
        5,29,0,0,143,144,3,18,9,0,144,17,1,0,0,0,145,146,3,26,13,0,146,150,
        5,37,0,0,147,151,3,28,14,0,148,151,3,58,29,0,149,151,3,60,30,0,150,
        147,1,0,0,0,150,148,1,0,0,0,150,149,1,0,0,0,151,152,1,0,0,0,152,
        153,5,36,0,0,153,19,1,0,0,0,154,155,3,44,22,0,155,156,3,62,31,0,
        156,171,5,20,0,0,157,159,5,29,0,0,158,157,1,0,0,0,158,159,1,0,0,
        0,159,160,1,0,0,0,160,168,3,26,13,0,161,163,5,27,0,0,162,164,5,29,
        0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,0,165,167,3,26,
        13,0,166,161,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,
        0,0,169,172,1,0,0,0,170,168,1,0,0,0,171,158,1,0,0,0,171,172,1,0,
        0,0,172,173,1,0,0,0,173,174,5,21,0,0,174,175,3,30,15,0,175,21,1,
        0,0,0,176,177,5,30,0,0,177,178,5,1,0,0,178,184,5,22,0,0,179,183,
        3,6,3,0,180,183,3,14,7,0,181,183,3,24,12,0,182,179,1,0,0,0,182,180,
        1,0,0,0,182,181,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,
        1,0,0,0,185,187,1,0,0,0,186,184,1,0,0,0,187,188,5,23,0,0,188,23,
        1,0,0,0,189,190,7,0,0,0,190,191,5,34,0,0,191,25,1,0,0,0,192,193,
        3,44,22,0,193,194,3,52,26,0,194,27,1,0,0,0,195,196,6,14,-1,0,196,
        197,5,55,0,0,197,208,3,28,14,7,198,199,7,1,0,0,199,208,3,28,14,5,
        200,201,5,20,0,0,201,202,3,28,14,0,202,203,5,21,0,0,203,208,1,0,
        0,0,204,208,3,52,26,0,205,208,3,42,21,0,206,208,3,50,25,0,207,195,
        1,0,0,0,207,198,1,0,0,0,207,200,1,0,0,0,207,204,1,0,0,0,207,205,
        1,0,0,0,207,206,1,0,0,0,208,240,1,0,0,0,209,210,10,15,0,0,210,211,
        7,2,0,0,211,239,3,28,14,16,212,213,10,14,0,0,213,214,7,3,0,0,214,
        239,3,28,14,15,215,216,10,13,0,0,216,217,7,4,0,0,217,239,3,28,14,
        14,218,219,10,12,0,0,219,220,7,5,0,0,220,239,3,28,14,13,221,222,
        10,11,0,0,222,223,7,6,0,0,223,239,3,28,14,12,224,225,10,10,0,0,225,
        226,7,7,0,0,226,239,3,28,14,11,227,228,10,9,0,0,228,229,7,8,0,0,
        229,239,3,28,14,10,230,231,10,8,0,0,231,232,5,57,0,0,232,233,3,28,
        14,0,233,234,5,34,0,0,234,235,3,28,14,9,235,239,1,0,0,0,236,237,
        10,6,0,0,237,239,7,1,0,0,238,209,1,0,0,0,238,212,1,0,0,0,238,215,
        1,0,0,0,238,218,1,0,0,0,238,221,1,0,0,0,238,224,1,0,0,0,238,227,
        1,0,0,0,238,230,1,0,0,0,238,236,1,0,0,0,239,242,1,0,0,0,240,238,
        1,0,0,0,240,241,1,0,0,0,241,29,1,0,0,0,242,240,1,0,0,0,243,247,5,
        22,0,0,244,246,3,32,16,0,245,244,1,0,0,0,246,249,1,0,0,0,247,245,
        1,0,0,0,247,248,1,0,0,0,248,250,1,0,0,0,249,247,1,0,0,0,250,251,
        5,23,0,0,251,31,1,0,0,0,252,306,3,6,3,0,253,306,3,14,7,0,254,255,
        3,40,20,0,255,256,5,36,0,0,256,306,1,0,0,0,257,258,3,28,14,0,258,
        259,5,36,0,0,259,306,1,0,0,0,260,261,3,42,21,0,261,262,5,36,0,0,
        262,306,1,0,0,0,263,264,5,13,0,0,264,265,5,20,0,0,265,266,3,34,17,
        0,266,269,5,21,0,0,267,270,3,32,16,0,268,270,3,30,15,0,269,267,1,
        0,0,0,269,268,1,0,0,0,270,276,1,0,0,0,271,274,5,14,0,0,272,275,3,
        32,16,0,273,275,3,30,15,0,274,272,1,0,0,0,274,273,1,0,0,0,275,277,
        1,0,0,0,276,271,1,0,0,0,276,277,1,0,0,0,277,306,1,0,0,0,278,279,
        5,16,0,0,279,280,5,20,0,0,280,281,3,34,17,0,281,284,5,21,0,0,282,
        285,3,32,16,0,283,285,3,30,15,0,284,282,1,0,0,0,284,283,1,0,0,0,
        285,306,1,0,0,0,286,287,5,15,0,0,287,288,5,20,0,0,288,290,3,36,18,
        0,289,291,3,34,17,0,290,289,1,0,0,0,290,291,1,0,0,0,291,292,1,0,
        0,0,292,294,5,36,0,0,293,295,3,38,19,0,294,293,1,0,0,0,294,295,1,
        0,0,0,295,296,1,0,0,0,296,299,5,21,0,0,297,300,3,32,16,0,298,300,
        3,30,15,0,299,297,1,0,0,0,299,298,1,0,0,0,300,306,1,0,0,0,301,302,
        5,17,0,0,302,303,3,28,14,0,303,304,5,36,0,0,304,306,1,0,0,0,305,
        252,1,0,0,0,305,253,1,0,0,0,305,254,1,0,0,0,305,257,1,0,0,0,305,
        260,1,0,0,0,305,263,1,0,0,0,305,278,1,0,0,0,305,286,1,0,0,0,305,
        301,1,0,0,0,306,33,1,0,0,0,307,308,3,28,14,0,308,35,1,0,0,0,309,
        314,3,10,5,0,310,314,3,18,9,0,311,314,3,32,16,0,312,314,5,36,0,0,
        313,309,1,0,0,0,313,310,1,0,0,0,313,311,1,0,0,0,313,312,1,0,0,0,
        314,37,1,0,0,0,315,318,3,28,14,0,316,318,3,40,20,0,317,315,1,0,0,
        0,317,316,1,0,0,0,318,39,1,0,0,0,319,320,3,52,26,0,320,324,5,37,
        0,0,321,325,3,28,14,0,322,325,3,58,29,0,323,325,3,60,30,0,324,321,
        1,0,0,0,324,322,1,0,0,0,324,323,1,0,0,0,325,41,1,0,0,0,326,329,3,
        52,26,0,327,329,5,1,0,0,328,326,1,0,0,0,328,327,1,0,0,0,329,330,
        1,0,0,0,330,339,5,20,0,0,331,336,3,28,14,0,332,333,5,27,0,0,333,
        335,3,28,14,0,334,332,1,0,0,0,335,338,1,0,0,0,336,334,1,0,0,0,336,
        337,1,0,0,0,337,340,1,0,0,0,338,336,1,0,0,0,339,331,1,0,0,0,339,
        340,1,0,0,0,340,341,1,0,0,0,341,342,5,21,0,0,342,43,1,0,0,0,343,
        346,3,46,23,0,344,346,3,48,24,0,345,343,1,0,0,0,345,344,1,0,0,0,
        346,45,1,0,0,0,347,348,7,9,0,0,348,47,1,0,0,0,349,350,3,46,23,0,
        350,352,5,24,0,0,351,353,3,28,14,0,352,351,1,0,0,0,352,353,1,0,0,
        0,353,354,1,0,0,0,354,355,5,25,0,0,355,49,1,0,0,0,356,357,7,10,0,
        0,357,51,1,0,0,0,358,359,3,66,33,0,359,360,5,35,0,0,360,362,1,0,
        0,0,361,358,1,0,0,0,361,362,1,0,0,0,362,368,1,0,0,0,363,364,3,64,
        32,0,364,365,5,28,0,0,365,367,1,0,0,0,366,363,1,0,0,0,367,370,1,
        0,0,0,368,366,1,0,0,0,368,369,1,0,0,0,369,372,1,0,0,0,370,368,1,
        0,0,0,371,373,7,11,0,0,372,371,1,0,0,0,372,373,1,0,0,0,373,376,1,
        0,0,0,374,377,3,54,27,0,375,377,3,56,28,0,376,374,1,0,0,0,376,375,
        1,0,0,0,377,53,1,0,0,0,378,379,5,1,0,0,379,55,1,0,0,0,380,386,5,
        1,0,0,381,383,5,24,0,0,382,384,3,28,14,0,383,382,1,0,0,0,383,384,
        1,0,0,0,384,385,1,0,0,0,385,387,5,25,0,0,386,381,1,0,0,0,387,388,
        1,0,0,0,388,386,1,0,0,0,388,389,1,0,0,0,389,57,1,0,0,0,390,399,5,
        22,0,0,391,396,3,58,29,0,392,393,5,27,0,0,393,395,3,58,29,0,394,
        392,1,0,0,0,395,398,1,0,0,0,396,394,1,0,0,0,396,397,1,0,0,0,397,
        400,1,0,0,0,398,396,1,0,0,0,399,391,1,0,0,0,399,400,1,0,0,0,400,
        401,1,0,0,0,401,404,5,23,0,0,402,404,3,28,14,0,403,390,1,0,0,0,403,
        402,1,0,0,0,404,59,1,0,0,0,405,406,5,18,0,0,406,411,3,44,22,0,407,
        408,5,24,0,0,408,409,3,28,14,0,409,410,5,25,0,0,410,412,1,0,0,0,
        411,407,1,0,0,0,411,412,1,0,0,0,412,61,1,0,0,0,413,414,3,66,33,0,
        414,415,5,35,0,0,415,417,1,0,0,0,416,413,1,0,0,0,416,417,1,0,0,0,
        417,423,1,0,0,0,418,419,3,64,32,0,419,420,5,28,0,0,420,422,1,0,0,
        0,421,418,1,0,0,0,422,425,1,0,0,0,423,421,1,0,0,0,423,424,1,0,0,
        0,424,426,1,0,0,0,425,423,1,0,0,0,426,427,5,1,0,0,427,63,1,0,0,0,
        428,446,3,54,27,0,429,446,3,56,28,0,430,443,5,1,0,0,431,440,5,20,
        0,0,432,437,3,28,14,0,433,434,5,27,0,0,434,436,3,28,14,0,435,433,
        1,0,0,0,436,439,1,0,0,0,437,435,1,0,0,0,437,438,1,0,0,0,438,441,
        1,0,0,0,439,437,1,0,0,0,440,432,1,0,0,0,440,441,1,0,0,0,441,442,
        1,0,0,0,442,444,5,21,0,0,443,431,1,0,0,0,443,444,1,0,0,0,444,446,
        1,0,0,0,445,428,1,0,0,0,445,429,1,0,0,0,445,430,1,0,0,0,446,65,1,
        0,0,0,447,448,5,1,0,0,448,67,1,0,0,0,57,71,73,81,89,92,96,101,113,
        116,121,124,129,132,140,150,158,163,168,171,182,184,207,238,240,
        247,269,274,276,284,290,294,299,305,313,317,324,328,336,339,345,
        352,361,368,372,376,383,388,396,399,403,411,416,423,437,440,443,
        445
    ]

class cpp_tinyParser ( Parser ):

    grammarFileName = "cpp_tiny.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'int'", "'float'", 
                     "'double'", "'char'", "'void'", "'bool'", "'if'", "'else'", 
                     "'for'", "'while'", "'return'", "'new'", "'#include'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "'\"'", "','", 
                     "'.'", "'const'", "'class'", "'public'", "'protected'", 
                     "'private'", "':'", "'::'", "';'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'++'", "'--'", "'%'", "'&'", "'|'", 
                     "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'&&'", 
                     "'||'", "'!'", "'^'", "'?'", "'<<'", "'>>'" ]

    symbolicNames = [ "<INVALID>", "NAME", "INT", "FLOAT", "CHAR", "STR", 
                      "BOOL", "TYPE_INT", "TYPE_FLOAT", "TYPE_DOUBLE", "TYPE_CHAR", 
                      "TYPE_VOID", "TYPE_BOOL", "IF", "ELSE", "FOR", "WHILE", 
                      "RETURN", "NEW", "INCLUDE", "L_BRACKET", "R_BRACKET", 
                      "L_BRACE", "R_BRACE", "L_SQUARE_BRACKET", "R_SQUARE_BRACKET", 
                      "QUOTE", "COMMA", "DOT", "CONSTANT", "CLASS", "PERMISSON_PUBLIC", 
                      "PERMISSON_PROTECTED", "PERMISSON_PRIVATE", "COLON", 
                      "DOUBLE_COLON", "SEMICOLON", "ASSIGN", "PLUS", "MINUS", 
                      "MULTIPLY", "DIVIDE", "DOUBLE_PLUS", "DOUBLE_MINUS", 
                      "MODULO", "AND", "OR", "LESS", "GREATER", "LEQ", "GEQ", 
                      "EQUAL", "NOT_EQUAL", "DOUBLE_AND", "DOUBLE_OR", "NOT", 
                      "XOR", "QUESTION", "SHIFT_LEFT", "SHIFT_RIGHT", "Skip", 
                      "CommentLine", "CommentBlock" ]

    RULE_prog = 0
    RULE_preProc = 1
    RULE_globalStatement = 2
    RULE_declaration = 3
    RULE_declarationConstant = 4
    RULE_declarationVariable = 5
    RULE_declarationFunction = 6
    RULE_definition = 7
    RULE_definitionConstant = 8
    RULE_definitionVariable = 9
    RULE_definitionFunction = 10
    RULE_classStatement = 11
    RULE_classPermission = 12
    RULE_variable = 13
    RULE_expression = 14
    RULE_block = 15
    RULE_statement = 16
    RULE_condition = 17
    RULE_forInit = 18
    RULE_forIter = 19
    RULE_assignment = 20
    RULE_call = 21
    RULE_type = 22
    RULE_simpleType = 23
    RULE_arrayType = 24
    RULE_typevalue = 25
    RULE_variableName = 26
    RULE_simpleVariable = 27
    RULE_arrayVariable = 28
    RULE_arrayValue = 29
    RULE_new = 30
    RULE_functionName = 31
    RULE_parentName = 32
    RULE_nameSpace = 33

    ruleNames =  [ "prog", "preProc", "globalStatement", "declaration", 
                   "declarationConstant", "declarationVariable", "declarationFunction", 
                   "definition", "definitionConstant", "definitionVariable", 
                   "definitionFunction", "classStatement", "classPermission", 
                   "variable", "expression", "block", "statement", "condition", 
                   "forInit", "forIter", "assignment", "call", "type", "simpleType", 
                   "arrayType", "typevalue", "variableName", "simpleVariable", 
                   "arrayVariable", "arrayValue", "new", "functionName", 
                   "parentName", "nameSpace" ]

    EOF = Token.EOF
    NAME=1
    INT=2
    FLOAT=3
    CHAR=4
    STR=5
    BOOL=6
    TYPE_INT=7
    TYPE_FLOAT=8
    TYPE_DOUBLE=9
    TYPE_CHAR=10
    TYPE_VOID=11
    TYPE_BOOL=12
    IF=13
    ELSE=14
    FOR=15
    WHILE=16
    RETURN=17
    NEW=18
    INCLUDE=19
    L_BRACKET=20
    R_BRACKET=21
    L_BRACE=22
    R_BRACE=23
    L_SQUARE_BRACKET=24
    R_SQUARE_BRACKET=25
    QUOTE=26
    COMMA=27
    DOT=28
    CONSTANT=29
    CLASS=30
    PERMISSON_PUBLIC=31
    PERMISSON_PROTECTED=32
    PERMISSON_PRIVATE=33
    COLON=34
    DOUBLE_COLON=35
    SEMICOLON=36
    ASSIGN=37
    PLUS=38
    MINUS=39
    MULTIPLY=40
    DIVIDE=41
    DOUBLE_PLUS=42
    DOUBLE_MINUS=43
    MODULO=44
    AND=45
    OR=46
    LESS=47
    GREATER=48
    LEQ=49
    GEQ=50
    EQUAL=51
    NOT_EQUAL=52
    DOUBLE_AND=53
    DOUBLE_OR=54
    NOT=55
    XOR=56
    QUESTION=57
    SHIFT_LEFT=58
    SHIFT_RIGHT=59
    Skip=60
    CommentLine=61
    CommentBlock=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preProc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.PreProcContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.PreProcContext,i)


        def globalStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.GlobalStatementContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.GlobalStatementContext,i)


        def classStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ClassStatementContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ClassStatementContext,i)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = cpp_tinyParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1611145090) != 0):
                self.state = 71
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [19]:
                    self.state = 68
                    self.preProc()
                    pass
                elif token in [1, 7, 8, 9, 10, 11, 12, 29]:
                    self.state = 69
                    self.globalStatement()
                    pass
                elif token in [30]:
                    self.state = 70
                    self.classStatement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreProcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE(self):
            return self.getToken(cpp_tinyParser.INCLUDE, 0)

        def LESS(self):
            return self.getToken(cpp_tinyParser.LESS, 0)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.NAME)
            else:
                return self.getToken(cpp_tinyParser.NAME, i)

        def GREATER(self):
            return self.getToken(cpp_tinyParser.GREATER, 0)

        def DOT(self):
            return self.getToken(cpp_tinyParser.DOT, 0)

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.QUOTE)
            else:
                return self.getToken(cpp_tinyParser.QUOTE, i)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_preProc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreProc" ):
                return visitor.visitPreProc(self)
            else:
                return visitor.visitChildren(self)




    def preProc(self):

        localctx = cpp_tinyParser.PreProcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_preProc)
        self._la = 0 # Token type
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(cpp_tinyParser.INCLUDE)
                self.state = 77
                self.match(cpp_tinyParser.LESS)
                self.state = 78
                self.match(cpp_tinyParser.NAME)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 79
                    self.match(cpp_tinyParser.DOT)
                    self.state = 80
                    self.match(cpp_tinyParser.NAME)


                self.state = 83
                self.match(cpp_tinyParser.GREATER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(cpp_tinyParser.INCLUDE)
                self.state = 85
                self.match(cpp_tinyParser.QUOTE)
                self.state = 86
                self.match(cpp_tinyParser.NAME)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 87
                    self.match(cpp_tinyParser.DOT)
                    self.state = 88
                    self.match(cpp_tinyParser.NAME)


                self.state = 91
                self.match(cpp_tinyParser.QUOTE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(cpp_tinyParser.DeclarationContext,0)


        def definition(self):
            return self.getTypedRuleContext(cpp_tinyParser.DefinitionContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_globalStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalStatement" ):
                return visitor.visitGlobalStatement(self)
            else:
                return visitor.visitChildren(self)




    def globalStatement(self):

        localctx = cpp_tinyParser.GlobalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_globalStatement)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.definition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationConstant(self):
            return self.getTypedRuleContext(cpp_tinyParser.DeclarationConstantContext,0)


        def declarationVariable(self):
            return self.getTypedRuleContext(cpp_tinyParser.DeclarationVariableContext,0)


        def declarationFunction(self):
            return self.getTypedRuleContext(cpp_tinyParser.DeclarationFunctionContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = cpp_tinyParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.declarationConstant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.declarationVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.declarationFunction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTANT(self):
            return self.getToken(cpp_tinyParser.CONSTANT, 0)

        def declarationVariable(self):
            return self.getTypedRuleContext(cpp_tinyParser.DeclarationVariableContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_declarationConstant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationConstant" ):
                return visitor.visitDeclarationConstant(self)
            else:
                return visitor.visitChildren(self)




    def declarationConstant(self):

        localctx = cpp_tinyParser.DeclarationConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declarationConstant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(cpp_tinyParser.CONSTANT)
            self.state = 104
            self.declarationVariable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(cpp_tinyParser.VariableContext,0)


        def SEMICOLON(self):
            return self.getToken(cpp_tinyParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_declarationVariable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationVariable" ):
                return visitor.visitDeclarationVariable(self)
            else:
                return visitor.visitChildren(self)




    def declarationVariable(self):

        localctx = cpp_tinyParser.DeclarationVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declarationVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.variable()
            self.state = 107
            self.match(cpp_tinyParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(cpp_tinyParser.TypeContext,0)


        def functionName(self):
            return self.getTypedRuleContext(cpp_tinyParser.FunctionNameContext,0)


        def L_BRACKET(self):
            return self.getToken(cpp_tinyParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(cpp_tinyParser.R_BRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(cpp_tinyParser.SEMICOLON, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.VariableContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.VariableContext,i)


        def CONSTANT(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.CONSTANT)
            else:
                return self.getToken(cpp_tinyParser.CONSTANT, i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.AND)
            else:
                return self.getToken(cpp_tinyParser.AND, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.COMMA)
            else:
                return self.getToken(cpp_tinyParser.COMMA, i)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_declarationFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationFunction" ):
                return visitor.visitDeclarationFunction(self)
            else:
                return visitor.visitChildren(self)




    def declarationFunction(self):

        localctx = cpp_tinyParser.DeclarationFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declarationFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.type_()
            self.state = 110
            self.functionName()
            self.state = 111
            self.match(cpp_tinyParser.L_BRACKET)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184908967810) != 0):
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 112
                    self.match(cpp_tinyParser.CONSTANT)


                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 115
                    self.match(cpp_tinyParser.AND)


                self.state = 118
                self.variable()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 119
                    self.match(cpp_tinyParser.COMMA)
                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==29:
                        self.state = 120
                        self.match(cpp_tinyParser.CONSTANT)


                    self.state = 124
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==45:
                        self.state = 123
                        self.match(cpp_tinyParser.AND)


                    self.state = 126
                    self.variable()
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 134
            self.match(cpp_tinyParser.R_BRACKET)
            self.state = 135
            self.match(cpp_tinyParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definitionConstant(self):
            return self.getTypedRuleContext(cpp_tinyParser.DefinitionConstantContext,0)


        def definitionVariable(self):
            return self.getTypedRuleContext(cpp_tinyParser.DefinitionVariableContext,0)


        def definitionFunction(self):
            return self.getTypedRuleContext(cpp_tinyParser.DefinitionFunctionContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition" ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def definition(self):

        localctx = cpp_tinyParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_definition)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.definitionConstant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.definitionVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.definitionFunction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTANT(self):
            return self.getToken(cpp_tinyParser.CONSTANT, 0)

        def definitionVariable(self):
            return self.getTypedRuleContext(cpp_tinyParser.DefinitionVariableContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_definitionConstant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinitionConstant" ):
                return visitor.visitDefinitionConstant(self)
            else:
                return visitor.visitChildren(self)




    def definitionConstant(self):

        localctx = cpp_tinyParser.DefinitionConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_definitionConstant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(cpp_tinyParser.CONSTANT)
            self.state = 143
            self.definitionVariable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(cpp_tinyParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(cpp_tinyParser.ASSIGN, 0)

        def SEMICOLON(self):
            return self.getToken(cpp_tinyParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,0)


        def arrayValue(self):
            return self.getTypedRuleContext(cpp_tinyParser.ArrayValueContext,0)


        def new(self):
            return self.getTypedRuleContext(cpp_tinyParser.NewContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_definitionVariable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinitionVariable" ):
                return visitor.visitDefinitionVariable(self)
            else:
                return visitor.visitChildren(self)




    def definitionVariable(self):

        localctx = cpp_tinyParser.DefinitionVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_definitionVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.variable()
            self.state = 146
            self.match(cpp_tinyParser.ASSIGN)
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 147
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 148
                self.arrayValue()
                pass

            elif la_ == 3:
                self.state = 149
                self.new()
                pass


            self.state = 152
            self.match(cpp_tinyParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(cpp_tinyParser.TypeContext,0)


        def functionName(self):
            return self.getTypedRuleContext(cpp_tinyParser.FunctionNameContext,0)


        def L_BRACKET(self):
            return self.getToken(cpp_tinyParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(cpp_tinyParser.R_BRACKET, 0)

        def block(self):
            return self.getTypedRuleContext(cpp_tinyParser.BlockContext,0)


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.VariableContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.VariableContext,i)


        def CONSTANT(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.CONSTANT)
            else:
                return self.getToken(cpp_tinyParser.CONSTANT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.COMMA)
            else:
                return self.getToken(cpp_tinyParser.COMMA, i)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_definitionFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinitionFunction" ):
                return visitor.visitDefinitionFunction(self)
            else:
                return visitor.visitChildren(self)




    def definitionFunction(self):

        localctx = cpp_tinyParser.DefinitionFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_definitionFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.type_()
            self.state = 155
            self.functionName()
            self.state = 156
            self.match(cpp_tinyParser.L_BRACKET)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536878978) != 0):
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 157
                    self.match(cpp_tinyParser.CONSTANT)


                self.state = 160
                self.variable()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 161
                    self.match(cpp_tinyParser.COMMA)
                    self.state = 163
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==29:
                        self.state = 162
                        self.match(cpp_tinyParser.CONSTANT)


                    self.state = 165
                    self.variable()
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 173
            self.match(cpp_tinyParser.R_BRACKET)
            self.state = 174
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(cpp_tinyParser.CLASS, 0)

        def NAME(self):
            return self.getToken(cpp_tinyParser.NAME, 0)

        def L_BRACE(self):
            return self.getToken(cpp_tinyParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(cpp_tinyParser.R_BRACE, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.DeclarationContext,i)


        def definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.DefinitionContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.DefinitionContext,i)


        def classPermission(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ClassPermissionContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ClassPermissionContext,i)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_classStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassStatement" ):
                return visitor.visitClassStatement(self)
            else:
                return visitor.visitChildren(self)




    def classStatement(self):

        localctx = cpp_tinyParser.ClassStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_classStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(cpp_tinyParser.CLASS)
            self.state = 177
            self.match(cpp_tinyParser.NAME)
            self.state = 178
            self.match(cpp_tinyParser.L_BRACE)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15569264514) != 0):
                self.state = 182
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 179
                    self.declaration()
                    pass

                elif la_ == 2:
                    self.state = 180
                    self.definition()
                    pass

                elif la_ == 3:
                    self.state = 181
                    self.classPermission()
                    pass


                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(cpp_tinyParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassPermissionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(cpp_tinyParser.COLON, 0)

        def PERMISSON_PUBLIC(self):
            return self.getToken(cpp_tinyParser.PERMISSON_PUBLIC, 0)

        def PERMISSON_PROTECTED(self):
            return self.getToken(cpp_tinyParser.PERMISSON_PROTECTED, 0)

        def PERMISSON_PRIVATE(self):
            return self.getToken(cpp_tinyParser.PERMISSON_PRIVATE, 0)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_classPermission

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassPermission" ):
                return visitor.visitClassPermission(self)
            else:
                return visitor.visitChildren(self)




    def classPermission(self):

        localctx = cpp_tinyParser.ClassPermissionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_classPermission)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 190
            self.match(cpp_tinyParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(cpp_tinyParser.TypeContext,0)


        def variableName(self):
            return self.getTypedRuleContext(cpp_tinyParser.VariableNameContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = cpp_tinyParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.type_()
            self.state = 193
            self.variableName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(cpp_tinyParser.NOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,i)


        def DOUBLE_PLUS(self):
            return self.getToken(cpp_tinyParser.DOUBLE_PLUS, 0)

        def DOUBLE_MINUS(self):
            return self.getToken(cpp_tinyParser.DOUBLE_MINUS, 0)

        def L_BRACKET(self):
            return self.getToken(cpp_tinyParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(cpp_tinyParser.R_BRACKET, 0)

        def variableName(self):
            return self.getTypedRuleContext(cpp_tinyParser.VariableNameContext,0)


        def call(self):
            return self.getTypedRuleContext(cpp_tinyParser.CallContext,0)


        def typevalue(self):
            return self.getTypedRuleContext(cpp_tinyParser.TypevalueContext,0)


        def PLUS(self):
            return self.getToken(cpp_tinyParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(cpp_tinyParser.MINUS, 0)

        def MULTIPLY(self):
            return self.getToken(cpp_tinyParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(cpp_tinyParser.DIVIDE, 0)

        def LESS(self):
            return self.getToken(cpp_tinyParser.LESS, 0)

        def GREATER(self):
            return self.getToken(cpp_tinyParser.GREATER, 0)

        def LEQ(self):
            return self.getToken(cpp_tinyParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(cpp_tinyParser.GEQ, 0)

        def NOT_EQUAL(self):
            return self.getToken(cpp_tinyParser.NOT_EQUAL, 0)

        def DOUBLE_AND(self):
            return self.getToken(cpp_tinyParser.DOUBLE_AND, 0)

        def DOUBLE_OR(self):
            return self.getToken(cpp_tinyParser.DOUBLE_OR, 0)

        def AND(self):
            return self.getToken(cpp_tinyParser.AND, 0)

        def OR(self):
            return self.getToken(cpp_tinyParser.OR, 0)

        def SHIFT_LEFT(self):
            return self.getToken(cpp_tinyParser.SHIFT_LEFT, 0)

        def SHIFT_RIGHT(self):
            return self.getToken(cpp_tinyParser.SHIFT_RIGHT, 0)

        def XOR(self):
            return self.getToken(cpp_tinyParser.XOR, 0)

        def MODULO(self):
            return self.getToken(cpp_tinyParser.MODULO, 0)

        def QUESTION(self):
            return self.getToken(cpp_tinyParser.QUESTION, 0)

        def COLON(self):
            return self.getToken(cpp_tinyParser.COLON, 0)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cpp_tinyParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 196
                self.match(cpp_tinyParser.NOT)
                self.state = 197
                self.expression(7)
                pass

            elif la_ == 2:
                self.state = 198
                _la = self._input.LA(1)
                if not(_la==42 or _la==43):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 199
                self.expression(5)
                pass

            elif la_ == 3:
                self.state = 200
                self.match(cpp_tinyParser.L_BRACKET)
                self.state = 201
                self.expression(0)
                self.state = 202
                self.match(cpp_tinyParser.R_BRACKET)
                pass

            elif la_ == 4:
                self.state = 204
                self.variableName()
                pass

            elif la_ == 5:
                self.state = 205
                self.call()
                pass

            elif la_ == 6:
                self.state = 206
                self.typevalue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 238
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 209
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 210
                        _la = self._input.LA(1)
                        if not(_la==38 or _la==39):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 211
                        self.expression(16)
                        pass

                    elif la_ == 2:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 212
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 213
                        _la = self._input.LA(1)
                        if not(_la==40 or _la==41):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 214
                        self.expression(15)
                        pass

                    elif la_ == 3:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 215
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 216
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6614661952700416) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 217
                        self.expression(14)
                        pass

                    elif la_ == 4:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 218
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 219
                        _la = self._input.LA(1)
                        if not(_la==53 or _la==54):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 220
                        self.expression(13)
                        pass

                    elif la_ == 5:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 221
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 222
                        _la = self._input.LA(1)
                        if not(_la==45 or _la==46):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 223
                        self.expression(12)
                        pass

                    elif la_ == 6:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 224
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 225
                        _la = self._input.LA(1)
                        if not(_la==58 or _la==59):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 226
                        self.expression(11)
                        pass

                    elif la_ == 7:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 227
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 228
                        _la = self._input.LA(1)
                        if not(_la==44 or _la==56):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 229
                        self.expression(10)
                        pass

                    elif la_ == 8:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 230
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 231
                        self.match(cpp_tinyParser.QUESTION)
                        self.state = 232
                        self.expression(0)
                        self.state = 233
                        self.match(cpp_tinyParser.COLON)
                        self.state = 234
                        self.expression(9)
                        pass

                    elif la_ == 9:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 236
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 237
                        _la = self._input.LA(1)
                        if not(_la==42 or _la==43):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACE(self):
            return self.getToken(cpp_tinyParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(cpp_tinyParser.R_BRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.StatementContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.StatementContext,i)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = cpp_tinyParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(cpp_tinyParser.L_BRACE)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 36078275580379134) != 0):
                self.state = 244
                self.statement()
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 250
            self.match(cpp_tinyParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(cpp_tinyParser.DeclarationContext,0)


        def definition(self):
            return self.getTypedRuleContext(cpp_tinyParser.DefinitionContext,0)


        def assignment(self):
            return self.getTypedRuleContext(cpp_tinyParser.AssignmentContext,0)


        def SEMICOLON(self):
            return self.getToken(cpp_tinyParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,0)


        def call(self):
            return self.getTypedRuleContext(cpp_tinyParser.CallContext,0)


        def IF(self):
            return self.getToken(cpp_tinyParser.IF, 0)

        def L_BRACKET(self):
            return self.getToken(cpp_tinyParser.L_BRACKET, 0)

        def condition(self):
            return self.getTypedRuleContext(cpp_tinyParser.ConditionContext,0)


        def R_BRACKET(self):
            return self.getToken(cpp_tinyParser.R_BRACKET, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.StatementContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.StatementContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.BlockContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(cpp_tinyParser.ELSE, 0)

        def WHILE(self):
            return self.getToken(cpp_tinyParser.WHILE, 0)

        def FOR(self):
            return self.getToken(cpp_tinyParser.FOR, 0)

        def forInit(self):
            return self.getTypedRuleContext(cpp_tinyParser.ForInitContext,0)


        def forIter(self):
            return self.getTypedRuleContext(cpp_tinyParser.ForIterContext,0)


        def RETURN(self):
            return self.getToken(cpp_tinyParser.RETURN, 0)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = cpp_tinyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.definition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.assignment()
                self.state = 255
                self.match(cpp_tinyParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 257
                self.expression(0)
                self.state = 258
                self.match(cpp_tinyParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 260
                self.call()
                self.state = 261
                self.match(cpp_tinyParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 263
                self.match(cpp_tinyParser.IF)
                self.state = 264
                self.match(cpp_tinyParser.L_BRACKET)
                self.state = 265
                self.condition()
                self.state = 266
                self.match(cpp_tinyParser.R_BRACKET)
                self.state = 269
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 20, 29, 40, 42, 43, 45, 55]:
                    self.state = 267
                    self.statement()
                    pass
                elif token in [22]:
                    self.state = 268
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 276
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 271
                    self.match(cpp_tinyParser.ELSE)
                    self.state = 274
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 20, 29, 40, 42, 43, 45, 55]:
                        self.state = 272
                        self.statement()
                        pass
                    elif token in [22]:
                        self.state = 273
                        self.block()
                        pass
                    else:
                        raise NoViableAltException(self)



                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 278
                self.match(cpp_tinyParser.WHILE)
                self.state = 279
                self.match(cpp_tinyParser.L_BRACKET)
                self.state = 280
                self.condition()
                self.state = 281
                self.match(cpp_tinyParser.R_BRACKET)
                self.state = 284
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 20, 29, 40, 42, 43, 45, 55]:
                    self.state = 282
                    self.statement()
                    pass
                elif token in [22]:
                    self.state = 283
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 286
                self.match(cpp_tinyParser.FOR)
                self.state = 287
                self.match(cpp_tinyParser.L_BRACKET)
                self.state = 288
                self.forInit()
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36078275043262590) != 0):
                    self.state = 289
                    self.condition()


                self.state = 292
                self.match(cpp_tinyParser.SEMICOLON)
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36078275043262590) != 0):
                    self.state = 293
                    self.forIter()


                self.state = 296
                self.match(cpp_tinyParser.R_BRACKET)
                self.state = 299
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 20, 29, 40, 42, 43, 45, 55]:
                    self.state = 297
                    self.statement()
                    pass
                elif token in [22]:
                    self.state = 298
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 301
                self.match(cpp_tinyParser.RETURN)
                self.state = 302
                self.expression(0)
                self.state = 303
                self.match(cpp_tinyParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = cpp_tinyParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationVariable(self):
            return self.getTypedRuleContext(cpp_tinyParser.DeclarationVariableContext,0)


        def definitionVariable(self):
            return self.getTypedRuleContext(cpp_tinyParser.DefinitionVariableContext,0)


        def statement(self):
            return self.getTypedRuleContext(cpp_tinyParser.StatementContext,0)


        def SEMICOLON(self):
            return self.getToken(cpp_tinyParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_forInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = cpp_tinyParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_forInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 309
                self.declarationVariable()
                pass

            elif la_ == 2:
                self.state = 310
                self.definitionVariable()
                pass

            elif la_ == 3:
                self.state = 311
                self.statement()
                pass

            elif la_ == 4:
                self.state = 312
                self.match(cpp_tinyParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForIterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,0)


        def assignment(self):
            return self.getTypedRuleContext(cpp_tinyParser.AssignmentContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_forIter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForIter" ):
                return visitor.visitForIter(self)
            else:
                return visitor.visitChildren(self)




    def forIter(self):

        localctx = cpp_tinyParser.ForIterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_forIter)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableName(self):
            return self.getTypedRuleContext(cpp_tinyParser.VariableNameContext,0)


        def ASSIGN(self):
            return self.getToken(cpp_tinyParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,0)


        def arrayValue(self):
            return self.getTypedRuleContext(cpp_tinyParser.ArrayValueContext,0)


        def new(self):
            return self.getTypedRuleContext(cpp_tinyParser.NewContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = cpp_tinyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.variableName()
            self.state = 320
            self.match(cpp_tinyParser.ASSIGN)
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 321
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 322
                self.arrayValue()
                pass

            elif la_ == 3:
                self.state = 323
                self.new()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(cpp_tinyParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(cpp_tinyParser.R_BRACKET, 0)

        def variableName(self):
            return self.getTypedRuleContext(cpp_tinyParser.VariableNameContext,0)


        def NAME(self):
            return self.getToken(cpp_tinyParser.NAME, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.COMMA)
            else:
                return self.getToken(cpp_tinyParser.COMMA, i)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = cpp_tinyParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 326
                self.variableName()
                pass

            elif la_ == 2:
                self.state = 327
                self.match(cpp_tinyParser.NAME)
                pass


            self.state = 330
            self.match(cpp_tinyParser.L_BRACKET)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36078275043262590) != 0):
                self.state = 331
                self.expression(0)
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 332
                    self.match(cpp_tinyParser.COMMA)
                    self.state = 333
                    self.expression(0)
                    self.state = 338
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 341
            self.match(cpp_tinyParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleType(self):
            return self.getTypedRuleContext(cpp_tinyParser.SimpleTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(cpp_tinyParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = cpp_tinyParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_type)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.simpleType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.arrayType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_INT(self):
            return self.getToken(cpp_tinyParser.TYPE_INT, 0)

        def TYPE_FLOAT(self):
            return self.getToken(cpp_tinyParser.TYPE_FLOAT, 0)

        def TYPE_DOUBLE(self):
            return self.getToken(cpp_tinyParser.TYPE_DOUBLE, 0)

        def TYPE_BOOL(self):
            return self.getToken(cpp_tinyParser.TYPE_BOOL, 0)

        def TYPE_CHAR(self):
            return self.getToken(cpp_tinyParser.TYPE_CHAR, 0)

        def TYPE_VOID(self):
            return self.getToken(cpp_tinyParser.TYPE_VOID, 0)

        def NAME(self):
            return self.getToken(cpp_tinyParser.NAME, 0)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_simpleType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleType" ):
                return visitor.visitSimpleType(self)
            else:
                return visitor.visitChildren(self)




    def simpleType(self):

        localctx = cpp_tinyParser.SimpleTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_simpleType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8066) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleType(self):
            return self.getTypedRuleContext(cpp_tinyParser.SimpleTypeContext,0)


        def L_SQUARE_BRACKET(self):
            return self.getToken(cpp_tinyParser.L_SQUARE_BRACKET, 0)

        def R_SQUARE_BRACKET(self):
            return self.getToken(cpp_tinyParser.R_SQUARE_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = cpp_tinyParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.simpleType()
            self.state = 350
            self.match(cpp_tinyParser.L_SQUARE_BRACKET)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36078275043262590) != 0):
                self.state = 351
                self.expression(0)


            self.state = 354
            self.match(cpp_tinyParser.R_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypevalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(cpp_tinyParser.INT, 0)

        def FLOAT(self):
            return self.getToken(cpp_tinyParser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(cpp_tinyParser.CHAR, 0)

        def STR(self):
            return self.getToken(cpp_tinyParser.STR, 0)

        def BOOL(self):
            return self.getToken(cpp_tinyParser.BOOL, 0)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_typevalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypevalue" ):
                return visitor.visitTypevalue(self)
            else:
                return visitor.visitChildren(self)




    def typevalue(self):

        localctx = cpp_tinyParser.TypevalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_typevalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleVariable(self):
            return self.getTypedRuleContext(cpp_tinyParser.SimpleVariableContext,0)


        def arrayVariable(self):
            return self.getTypedRuleContext(cpp_tinyParser.ArrayVariableContext,0)


        def nameSpace(self):
            return self.getTypedRuleContext(cpp_tinyParser.NameSpaceContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(cpp_tinyParser.DOUBLE_COLON, 0)

        def parentName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ParentNameContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ParentNameContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.DOT)
            else:
                return self.getToken(cpp_tinyParser.DOT, i)

        def MULTIPLY(self):
            return self.getToken(cpp_tinyParser.MULTIPLY, 0)

        def AND(self):
            return self.getToken(cpp_tinyParser.AND, 0)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_variableName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableName" ):
                return visitor.visitVariableName(self)
            else:
                return visitor.visitChildren(self)




    def variableName(self):

        localctx = cpp_tinyParser.VariableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_variableName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 358
                self.nameSpace()
                self.state = 359
                self.match(cpp_tinyParser.DOUBLE_COLON)


            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 363
                    self.parentName()
                    self.state = 364
                    self.match(cpp_tinyParser.DOT) 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40 or _la==45:
                self.state = 371
                _la = self._input.LA(1)
                if not(_la==40 or _la==45):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 374
                self.simpleVariable()
                pass

            elif la_ == 2:
                self.state = 375
                self.arrayVariable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(cpp_tinyParser.NAME, 0)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_simpleVariable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleVariable" ):
                return visitor.visitSimpleVariable(self)
            else:
                return visitor.visitChildren(self)




    def simpleVariable(self):

        localctx = cpp_tinyParser.SimpleVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_simpleVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(cpp_tinyParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(cpp_tinyParser.NAME, 0)

        def L_SQUARE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.L_SQUARE_BRACKET)
            else:
                return self.getToken(cpp_tinyParser.L_SQUARE_BRACKET, i)

        def R_SQUARE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.R_SQUARE_BRACKET)
            else:
                return self.getToken(cpp_tinyParser.R_SQUARE_BRACKET, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,i)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_arrayVariable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayVariable" ):
                return visitor.visitArrayVariable(self)
            else:
                return visitor.visitChildren(self)




    def arrayVariable(self):

        localctx = cpp_tinyParser.ArrayVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arrayVariable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(cpp_tinyParser.NAME)
            self.state = 386 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 381
                    self.match(cpp_tinyParser.L_SQUARE_BRACKET)
                    self.state = 383
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36078275043262590) != 0):
                        self.state = 382
                        self.expression(0)


                    self.state = 385
                    self.match(cpp_tinyParser.R_SQUARE_BRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 388 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACE(self):
            return self.getToken(cpp_tinyParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(cpp_tinyParser.R_BRACE, 0)

        def arrayValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ArrayValueContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ArrayValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.COMMA)
            else:
                return self.getToken(cpp_tinyParser.COMMA, i)

        def expression(self):
            return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return cpp_tinyParser.RULE_arrayValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayValue" ):
                return visitor.visitArrayValue(self)
            else:
                return visitor.visitChildren(self)




    def arrayValue(self):

        localctx = cpp_tinyParser.ArrayValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_arrayValue)
        self._la = 0 # Token type
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(cpp_tinyParser.L_BRACE)
                self.state = 399
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36078275047456894) != 0):
                    self.state = 391
                    self.arrayValue()
                    self.state = 396
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==27:
                        self.state = 392
                        self.match(cpp_tinyParser.COMMA)
                        self.state = 393
                        self.arrayValue()
                        self.state = 398
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 401
                self.match(cpp_tinyParser.R_BRACE)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 20, 40, 42, 43, 45, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(cpp_tinyParser.NEW, 0)

        def type_(self):
            return self.getTypedRuleContext(cpp_tinyParser.TypeContext,0)


        def L_SQUARE_BRACKET(self):
            return self.getToken(cpp_tinyParser.L_SQUARE_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,0)


        def R_SQUARE_BRACKET(self):
            return self.getToken(cpp_tinyParser.R_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_new

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew" ):
                return visitor.visitNew(self)
            else:
                return visitor.visitChildren(self)




    def new(self):

        localctx = cpp_tinyParser.NewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_new)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(cpp_tinyParser.NEW)
            self.state = 406
            self.type_()
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 407
                self.match(cpp_tinyParser.L_SQUARE_BRACKET)
                self.state = 408
                self.expression(0)
                self.state = 409
                self.match(cpp_tinyParser.R_SQUARE_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(cpp_tinyParser.NAME, 0)

        def nameSpace(self):
            return self.getTypedRuleContext(cpp_tinyParser.NameSpaceContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(cpp_tinyParser.DOUBLE_COLON, 0)

        def parentName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ParentNameContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ParentNameContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.DOT)
            else:
                return self.getToken(cpp_tinyParser.DOT, i)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_functionName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionName" ):
                return visitor.visitFunctionName(self)
            else:
                return visitor.visitChildren(self)




    def functionName(self):

        localctx = cpp_tinyParser.FunctionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_functionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 413
                self.nameSpace()
                self.state = 414
                self.match(cpp_tinyParser.DOUBLE_COLON)


            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 418
                    self.parentName()
                    self.state = 419
                    self.match(cpp_tinyParser.DOT) 
                self.state = 425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

            self.state = 426
            self.match(cpp_tinyParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParentNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleVariable(self):
            return self.getTypedRuleContext(cpp_tinyParser.SimpleVariableContext,0)


        def arrayVariable(self):
            return self.getTypedRuleContext(cpp_tinyParser.ArrayVariableContext,0)


        def NAME(self):
            return self.getToken(cpp_tinyParser.NAME, 0)

        def L_BRACKET(self):
            return self.getToken(cpp_tinyParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(cpp_tinyParser.R_BRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.COMMA)
            else:
                return self.getToken(cpp_tinyParser.COMMA, i)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_parentName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentName" ):
                return visitor.visitParentName(self)
            else:
                return visitor.visitChildren(self)




    def parentName(self):

        localctx = cpp_tinyParser.ParentNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_parentName)
        self._la = 0 # Token type
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.simpleVariable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.arrayVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 430
                self.match(cpp_tinyParser.NAME)
                self.state = 443
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 431
                    self.match(cpp_tinyParser.L_BRACKET)
                    self.state = 440
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36078275043262590) != 0):
                        self.state = 432
                        self.expression(0)
                        self.state = 437
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==27:
                            self.state = 433
                            self.match(cpp_tinyParser.COMMA)
                            self.state = 434
                            self.expression(0)
                            self.state = 439
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)



                    self.state = 442
                    self.match(cpp_tinyParser.R_BRACKET)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameSpaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(cpp_tinyParser.NAME, 0)

        def getRuleIndex(self):
            return cpp_tinyParser.RULE_nameSpace

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameSpace" ):
                return visitor.visitNameSpace(self)
            else:
                return visitor.visitChildren(self)




    def nameSpace(self):

        localctx = cpp_tinyParser.NameSpaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_nameSpace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(cpp_tinyParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         




