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
        4,1,59,439,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,5,0,72,8,0,10,0,12,0,75,9,0,1,1,1,1,1,1,1,1,1,1,
        3,1,82,8,1,1,1,1,1,1,2,1,2,3,2,88,8,2,1,3,1,3,1,3,3,3,93,8,3,1,4,
        1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,105,8,6,1,6,3,6,108,8,6,
        1,6,1,6,1,6,3,6,113,8,6,1,6,3,6,116,8,6,1,6,5,6,119,8,6,10,6,12,
        6,122,9,6,3,6,124,8,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,132,8,7,1,8,1,
        8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,142,8,9,1,9,1,9,1,10,1,10,1,10,1,10,
        3,10,150,8,10,1,10,1,10,1,10,3,10,155,8,10,1,10,5,10,158,8,10,10,
        10,12,10,161,9,10,3,10,163,8,10,1,10,1,10,1,10,1,11,1,11,1,11,1,
        11,1,11,1,11,5,11,174,8,11,10,11,12,11,177,9,11,1,11,1,11,1,12,1,
        12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,3,14,197,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,228,8,14,10,14,12,14,
        231,9,14,1,15,1,15,5,15,235,8,15,10,15,12,15,238,9,15,1,15,1,15,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,3,16,259,8,16,1,16,1,16,1,16,3,16,264,8,16,3,
        16,266,8,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,274,8,16,1,16,1,16,
        1,16,1,16,3,16,280,8,16,1,16,1,16,3,16,284,8,16,1,16,1,16,1,16,3,
        16,289,8,16,1,16,1,16,1,16,1,16,3,16,295,8,16,1,17,1,17,1,18,1,18,
        1,18,1,18,3,18,303,8,18,1,19,1,19,3,19,307,8,19,1,20,1,20,1,20,1,
        20,1,20,3,20,314,8,20,1,21,1,21,3,21,318,8,21,1,21,1,21,1,21,1,21,
        5,21,324,8,21,10,21,12,21,327,9,21,3,21,329,8,21,1,21,1,21,1,22,
        1,22,3,22,335,8,22,1,23,1,23,1,24,1,24,1,24,3,24,342,8,24,1,24,1,
        24,1,25,1,25,1,26,1,26,1,26,3,26,351,8,26,1,26,1,26,1,26,5,26,356,
        8,26,10,26,12,26,359,9,26,1,26,3,26,362,8,26,1,26,1,26,3,26,366,
        8,26,1,27,1,27,1,28,1,28,1,28,3,28,373,8,28,1,28,4,28,376,8,28,11,
        28,12,28,377,1,29,1,29,1,29,1,29,5,29,384,8,29,10,29,12,29,387,9,
        29,3,29,389,8,29,1,29,1,29,3,29,393,8,29,1,30,1,30,1,30,1,30,1,30,
        1,30,3,30,401,8,30,1,31,1,31,1,31,3,31,406,8,31,1,31,1,31,1,31,5,
        31,411,8,31,10,31,12,31,414,9,31,1,31,1,31,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,5,32,425,8,32,10,32,12,32,428,9,32,3,32,430,8,32,1,
        32,3,32,433,8,32,3,32,435,8,32,1,33,1,33,1,33,0,1,28,34,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,66,0,12,1,0,15,17,1,0,35,36,1,0,19,20,1,0,21,
        22,3,0,2,2,4,4,23,26,1,0,27,28,2,0,8,8,29,29,1,0,30,31,1,0,32,33,
        2,0,42,46,51,51,1,0,52,56,2,0,8,8,21,21,485,0,73,1,0,0,0,2,76,1,
        0,0,0,4,87,1,0,0,0,6,92,1,0,0,0,8,94,1,0,0,0,10,97,1,0,0,0,12,100,
        1,0,0,0,14,131,1,0,0,0,16,133,1,0,0,0,18,136,1,0,0,0,20,145,1,0,
        0,0,22,167,1,0,0,0,24,180,1,0,0,0,26,183,1,0,0,0,28,196,1,0,0,0,
        30,232,1,0,0,0,32,294,1,0,0,0,34,296,1,0,0,0,36,302,1,0,0,0,38,306,
        1,0,0,0,40,308,1,0,0,0,42,317,1,0,0,0,44,334,1,0,0,0,46,336,1,0,
        0,0,48,338,1,0,0,0,50,345,1,0,0,0,52,350,1,0,0,0,54,367,1,0,0,0,
        56,369,1,0,0,0,58,392,1,0,0,0,60,394,1,0,0,0,62,405,1,0,0,0,64,434,
        1,0,0,0,66,436,1,0,0,0,68,72,3,2,1,0,69,72,3,4,2,0,70,72,3,22,11,
        0,71,68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,
        1,0,0,0,73,74,1,0,0,0,74,1,1,0,0,0,75,73,1,0,0,0,76,77,5,1,0,0,77,
        78,5,2,0,0,78,81,5,51,0,0,79,80,5,3,0,0,80,82,5,51,0,0,81,79,1,0,
        0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,84,5,4,0,0,84,3,1,0,0,0,85,88,
        3,6,3,0,86,88,3,14,7,0,87,85,1,0,0,0,87,86,1,0,0,0,88,5,1,0,0,0,
        89,93,3,8,4,0,90,93,3,10,5,0,91,93,3,12,6,0,92,89,1,0,0,0,92,90,
        1,0,0,0,92,91,1,0,0,0,93,7,1,0,0,0,94,95,5,5,0,0,95,96,3,10,5,0,
        96,9,1,0,0,0,97,98,3,26,13,0,98,99,5,6,0,0,99,11,1,0,0,0,100,101,
        3,44,22,0,101,102,3,62,31,0,102,123,5,7,0,0,103,105,5,5,0,0,104,
        103,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,108,5,8,0,0,107,
        106,1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,120,3,26,13,0,110,
        112,5,9,0,0,111,113,5,5,0,0,112,111,1,0,0,0,112,113,1,0,0,0,113,
        115,1,0,0,0,114,116,5,8,0,0,115,114,1,0,0,0,115,116,1,0,0,0,116,
        117,1,0,0,0,117,119,3,26,13,0,118,110,1,0,0,0,119,122,1,0,0,0,120,
        118,1,0,0,0,120,121,1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,123,
        104,1,0,0,0,123,124,1,0,0,0,124,125,1,0,0,0,125,126,5,10,0,0,126,
        127,5,6,0,0,127,13,1,0,0,0,128,132,3,16,8,0,129,132,3,18,9,0,130,
        132,3,20,10,0,131,128,1,0,0,0,131,129,1,0,0,0,131,130,1,0,0,0,132,
        15,1,0,0,0,133,134,5,5,0,0,134,135,3,18,9,0,135,17,1,0,0,0,136,137,
        3,26,13,0,137,141,5,11,0,0,138,142,3,28,14,0,139,142,3,58,29,0,140,
        142,3,60,30,0,141,138,1,0,0,0,141,139,1,0,0,0,141,140,1,0,0,0,142,
        143,1,0,0,0,143,144,5,6,0,0,144,19,1,0,0,0,145,146,3,44,22,0,146,
        147,3,62,31,0,147,162,5,7,0,0,148,150,5,5,0,0,149,148,1,0,0,0,149,
        150,1,0,0,0,150,151,1,0,0,0,151,159,3,26,13,0,152,154,5,9,0,0,153,
        155,5,5,0,0,154,153,1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,
        158,3,26,13,0,157,152,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,
        160,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,162,149,1,0,0,0,162,
        163,1,0,0,0,163,164,1,0,0,0,164,165,5,10,0,0,165,166,3,30,15,0,166,
        21,1,0,0,0,167,168,5,12,0,0,168,169,5,51,0,0,169,175,5,13,0,0,170,
        174,3,6,3,0,171,174,3,14,7,0,172,174,3,24,12,0,173,170,1,0,0,0,173,
        171,1,0,0,0,173,172,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,
        176,1,0,0,0,176,178,1,0,0,0,177,175,1,0,0,0,178,179,5,14,0,0,179,
        23,1,0,0,0,180,181,7,0,0,0,181,182,5,18,0,0,182,25,1,0,0,0,183,184,
        3,44,22,0,184,185,3,52,26,0,185,27,1,0,0,0,186,187,6,14,-1,0,187,
        188,7,1,0,0,188,197,3,28,14,5,189,190,5,7,0,0,190,191,3,28,14,0,
        191,192,5,10,0,0,192,197,1,0,0,0,193,197,3,52,26,0,194,197,3,42,
        21,0,195,197,3,50,25,0,196,186,1,0,0,0,196,189,1,0,0,0,196,193,1,
        0,0,0,196,194,1,0,0,0,196,195,1,0,0,0,197,229,1,0,0,0,198,199,10,
        14,0,0,199,200,7,2,0,0,200,228,3,28,14,15,201,202,10,13,0,0,202,
        203,7,3,0,0,203,228,3,28,14,14,204,205,10,12,0,0,205,206,7,4,0,0,
        206,228,3,28,14,13,207,208,10,11,0,0,208,209,7,5,0,0,209,228,3,28,
        14,12,210,211,10,10,0,0,211,212,7,6,0,0,212,228,3,28,14,11,213,214,
        10,9,0,0,214,215,7,7,0,0,215,228,3,28,14,10,216,217,10,8,0,0,217,
        218,7,8,0,0,218,228,3,28,14,9,219,220,10,7,0,0,220,221,5,34,0,0,
        221,222,3,28,14,0,222,223,5,18,0,0,223,224,3,28,14,8,224,228,1,0,
        0,0,225,226,10,6,0,0,226,228,7,1,0,0,227,198,1,0,0,0,227,201,1,0,
        0,0,227,204,1,0,0,0,227,207,1,0,0,0,227,210,1,0,0,0,227,213,1,0,
        0,0,227,216,1,0,0,0,227,219,1,0,0,0,227,225,1,0,0,0,228,231,1,0,
        0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,29,1,0,0,0,231,229,1,0,0,
        0,232,236,5,13,0,0,233,235,3,32,16,0,234,233,1,0,0,0,235,238,1,0,
        0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,239,1,0,0,0,238,236,1,0,
        0,0,239,240,5,14,0,0,240,31,1,0,0,0,241,295,3,6,3,0,242,295,3,14,
        7,0,243,244,3,40,20,0,244,245,5,6,0,0,245,295,1,0,0,0,246,247,3,
        28,14,0,247,248,5,6,0,0,248,295,1,0,0,0,249,250,3,42,21,0,250,251,
        5,6,0,0,251,295,1,0,0,0,252,253,5,37,0,0,253,254,5,7,0,0,254,255,
        3,34,17,0,255,258,5,10,0,0,256,259,3,32,16,0,257,259,3,30,15,0,258,
        256,1,0,0,0,258,257,1,0,0,0,259,265,1,0,0,0,260,263,5,38,0,0,261,
        264,3,32,16,0,262,264,3,30,15,0,263,261,1,0,0,0,263,262,1,0,0,0,
        264,266,1,0,0,0,265,260,1,0,0,0,265,266,1,0,0,0,266,295,1,0,0,0,
        267,268,5,39,0,0,268,269,5,7,0,0,269,270,3,34,17,0,270,273,5,10,
        0,0,271,274,3,32,16,0,272,274,3,30,15,0,273,271,1,0,0,0,273,272,
        1,0,0,0,274,295,1,0,0,0,275,276,5,40,0,0,276,277,5,7,0,0,277,279,
        3,36,18,0,278,280,3,34,17,0,279,278,1,0,0,0,279,280,1,0,0,0,280,
        281,1,0,0,0,281,283,5,6,0,0,282,284,3,38,19,0,283,282,1,0,0,0,283,
        284,1,0,0,0,284,285,1,0,0,0,285,288,5,10,0,0,286,289,3,32,16,0,287,
        289,3,30,15,0,288,286,1,0,0,0,288,287,1,0,0,0,289,295,1,0,0,0,290,
        291,5,41,0,0,291,292,3,28,14,0,292,293,5,6,0,0,293,295,1,0,0,0,294,
        241,1,0,0,0,294,242,1,0,0,0,294,243,1,0,0,0,294,246,1,0,0,0,294,
        249,1,0,0,0,294,252,1,0,0,0,294,267,1,0,0,0,294,275,1,0,0,0,294,
        290,1,0,0,0,295,33,1,0,0,0,296,297,3,28,14,0,297,35,1,0,0,0,298,
        303,3,10,5,0,299,303,3,18,9,0,300,303,3,32,16,0,301,303,5,6,0,0,
        302,298,1,0,0,0,302,299,1,0,0,0,302,300,1,0,0,0,302,301,1,0,0,0,
        303,37,1,0,0,0,304,307,3,28,14,0,305,307,3,40,20,0,306,304,1,0,0,
        0,306,305,1,0,0,0,307,39,1,0,0,0,308,309,3,52,26,0,309,313,5,11,
        0,0,310,314,3,28,14,0,311,314,3,58,29,0,312,314,3,60,30,0,313,310,
        1,0,0,0,313,311,1,0,0,0,313,312,1,0,0,0,314,41,1,0,0,0,315,318,3,
        52,26,0,316,318,5,51,0,0,317,315,1,0,0,0,317,316,1,0,0,0,318,319,
        1,0,0,0,319,328,5,7,0,0,320,325,3,28,14,0,321,322,5,9,0,0,322,324,
        3,28,14,0,323,321,1,0,0,0,324,327,1,0,0,0,325,323,1,0,0,0,325,326,
        1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,328,320,1,0,0,0,328,329,
        1,0,0,0,329,330,1,0,0,0,330,331,5,10,0,0,331,43,1,0,0,0,332,335,
        3,46,23,0,333,335,3,48,24,0,334,332,1,0,0,0,334,333,1,0,0,0,335,
        45,1,0,0,0,336,337,7,9,0,0,337,47,1,0,0,0,338,339,3,46,23,0,339,
        341,5,47,0,0,340,342,3,28,14,0,341,340,1,0,0,0,341,342,1,0,0,0,342,
        343,1,0,0,0,343,344,5,48,0,0,344,49,1,0,0,0,345,346,7,10,0,0,346,
        51,1,0,0,0,347,348,3,66,33,0,348,349,5,49,0,0,349,351,1,0,0,0,350,
        347,1,0,0,0,350,351,1,0,0,0,351,357,1,0,0,0,352,353,3,64,32,0,353,
        354,5,3,0,0,354,356,1,0,0,0,355,352,1,0,0,0,356,359,1,0,0,0,357,
        355,1,0,0,0,357,358,1,0,0,0,358,361,1,0,0,0,359,357,1,0,0,0,360,
        362,7,11,0,0,361,360,1,0,0,0,361,362,1,0,0,0,362,365,1,0,0,0,363,
        366,3,54,27,0,364,366,3,56,28,0,365,363,1,0,0,0,365,364,1,0,0,0,
        366,53,1,0,0,0,367,368,5,51,0,0,368,55,1,0,0,0,369,375,5,51,0,0,
        370,372,5,47,0,0,371,373,3,28,14,0,372,371,1,0,0,0,372,373,1,0,0,
        0,373,374,1,0,0,0,374,376,5,48,0,0,375,370,1,0,0,0,376,377,1,0,0,
        0,377,375,1,0,0,0,377,378,1,0,0,0,378,57,1,0,0,0,379,388,5,13,0,
        0,380,385,3,58,29,0,381,382,5,9,0,0,382,384,3,58,29,0,383,381,1,
        0,0,0,384,387,1,0,0,0,385,383,1,0,0,0,385,386,1,0,0,0,386,389,1,
        0,0,0,387,385,1,0,0,0,388,380,1,0,0,0,388,389,1,0,0,0,389,390,1,
        0,0,0,390,393,5,14,0,0,391,393,3,28,14,0,392,379,1,0,0,0,392,391,
        1,0,0,0,393,59,1,0,0,0,394,395,5,50,0,0,395,400,3,44,22,0,396,397,
        5,47,0,0,397,398,3,28,14,0,398,399,5,48,0,0,399,401,1,0,0,0,400,
        396,1,0,0,0,400,401,1,0,0,0,401,61,1,0,0,0,402,403,3,66,33,0,403,
        404,5,49,0,0,404,406,1,0,0,0,405,402,1,0,0,0,405,406,1,0,0,0,406,
        412,1,0,0,0,407,408,3,64,32,0,408,409,5,3,0,0,409,411,1,0,0,0,410,
        407,1,0,0,0,411,414,1,0,0,0,412,410,1,0,0,0,412,413,1,0,0,0,413,
        415,1,0,0,0,414,412,1,0,0,0,415,416,5,51,0,0,416,63,1,0,0,0,417,
        435,3,54,27,0,418,435,3,56,28,0,419,432,5,51,0,0,420,429,5,7,0,0,
        421,426,3,28,14,0,422,423,5,9,0,0,423,425,3,28,14,0,424,422,1,0,
        0,0,425,428,1,0,0,0,426,424,1,0,0,0,426,427,1,0,0,0,427,430,1,0,
        0,0,428,426,1,0,0,0,429,421,1,0,0,0,429,430,1,0,0,0,430,431,1,0,
        0,0,431,433,5,10,0,0,432,420,1,0,0,0,432,433,1,0,0,0,433,435,1,0,
        0,0,434,417,1,0,0,0,434,418,1,0,0,0,434,419,1,0,0,0,435,65,1,0,0,
        0,436,437,5,51,0,0,437,67,1,0,0,0,55,71,73,81,87,92,104,107,112,
        115,120,123,131,141,149,154,159,162,173,175,196,227,229,236,258,
        263,265,273,279,283,288,294,302,306,313,317,325,328,334,341,350,
        357,361,365,372,377,385,388,392,400,405,412,426,429,432,434
    ]

class cpp_tinyParser ( Parser ):

    grammarFileName = "cpp_tiny.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#include'", "'<'", "'.'", "'>'", "'const'", 
                     "';'", "'('", "'&'", "','", "')'", "'='", "'class'", 
                     "'{'", "'}'", "'public'", "'protected'", "'private'", 
                     "':'", "'+'", "'-'", "'*'", "'/'", "'<='", "'>='", 
                     "'=='", "'!='", "'&&'", "'||'", "'|'", "'<<'", "'>>'", 
                     "'^'", "'%'", "'?'", "'++'", "'--'", "'if'", "'else'", 
                     "'while'", "'for'", "'return'", "'int'", "'float'", 
                     "'char'", "'void'", "'bool'", "'['", "']'", "'::'", 
                     "'new'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NAME", "INT", 
                      "FLOAT", "CHAR", "STR", "BOOL", "Skip", "CommentLine", 
                      "CommentBlock" ]

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
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    NAME=51
    INT=52
    FLOAT=53
    CHAR=54
    STR=55
    BOOL=56
    Skip=57
    CommentLine=58
    CommentBlock=59

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2388139255533602) != 0):
                self.state = 71
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 68
                    self.preProc()
                    pass
                elif token in [5, 42, 43, 44, 45, 46, 51]:
                    self.state = 69
                    self.globalStatement()
                    pass
                elif token in [12]:
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

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(cpp_tinyParser.NAME)
            else:
                return self.getToken(cpp_tinyParser.NAME, i)

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
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(cpp_tinyParser.T__0)
            self.state = 77
            self.match(cpp_tinyParser.T__1)
            self.state = 78
            self.match(cpp_tinyParser.NAME)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 79
                self.match(cpp_tinyParser.T__2)
                self.state = 80
                self.match(cpp_tinyParser.NAME)


            self.state = 83
            self.match(cpp_tinyParser.T__3)
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
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
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
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.declarationConstant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.declarationVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
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
            self.state = 94
            self.match(cpp_tinyParser.T__4)
            self.state = 95
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
            self.state = 97
            self.variable()
            self.state = 98
            self.match(cpp_tinyParser.T__5)
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


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.VariableContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.VariableContext,i)


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
            self.state = 100
            self.type_()
            self.state = 101
            self.functionName()
            self.state = 102
            self.match(cpp_tinyParser.T__6)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2388139255529760) != 0):
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 103
                    self.match(cpp_tinyParser.T__4)


                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 106
                    self.match(cpp_tinyParser.T__7)


                self.state = 109
                self.variable()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 110
                    self.match(cpp_tinyParser.T__8)
                    self.state = 112
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 111
                        self.match(cpp_tinyParser.T__4)


                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==8:
                        self.state = 114
                        self.match(cpp_tinyParser.T__7)


                    self.state = 117
                    self.variable()
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 125
            self.match(cpp_tinyParser.T__9)
            self.state = 126
            self.match(cpp_tinyParser.T__5)
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
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.definitionConstant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.definitionVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
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
            self.state = 133
            self.match(cpp_tinyParser.T__4)
            self.state = 134
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
            self.state = 136
            self.variable()
            self.state = 137
            self.match(cpp_tinyParser.T__10)
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 138
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 139
                self.arrayValue()
                pass

            elif la_ == 3:
                self.state = 140
                self.new()
                pass


            self.state = 143
            self.match(cpp_tinyParser.T__5)
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


        def block(self):
            return self.getTypedRuleContext(cpp_tinyParser.BlockContext,0)


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.VariableContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.VariableContext,i)


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
            self.state = 145
            self.type_()
            self.state = 146
            self.functionName()
            self.state = 147
            self.match(cpp_tinyParser.T__6)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2388139255529504) != 0):
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 148
                    self.match(cpp_tinyParser.T__4)


                self.state = 151
                self.variable()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 152
                    self.match(cpp_tinyParser.T__8)
                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 153
                        self.match(cpp_tinyParser.T__4)


                    self.state = 156
                    self.variable()
                    self.state = 161
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 164
            self.match(cpp_tinyParser.T__9)
            self.state = 165
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

        def NAME(self):
            return self.getToken(cpp_tinyParser.NAME, 0)

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
            self.state = 167
            self.match(cpp_tinyParser.T__11)
            self.state = 168
            self.match(cpp_tinyParser.NAME)
            self.state = 169
            self.match(cpp_tinyParser.T__12)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2388139255758880) != 0):
                self.state = 173
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 170
                    self.declaration()
                    pass

                elif la_ == 2:
                    self.state = 171
                    self.definition()
                    pass

                elif la_ == 3:
                    self.state = 172
                    self.classPermission()
                    pass


                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self.match(cpp_tinyParser.T__13)
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
            self.state = 180
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 181
            self.match(cpp_tinyParser.T__17)
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
            self.state = 183
            self.type_()
            self.state = 184
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,i)


        def variableName(self):
            return self.getTypedRuleContext(cpp_tinyParser.VariableNameContext,0)


        def call(self):
            return self.getTypedRuleContext(cpp_tinyParser.CallContext,0)


        def typevalue(self):
            return self.getTypedRuleContext(cpp_tinyParser.TypevalueContext,0)


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
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 187
                _la = self._input.LA(1)
                if not(_la==35 or _la==36):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 188
                self.expression(5)
                pass

            elif la_ == 2:
                self.state = 189
                self.match(cpp_tinyParser.T__6)
                self.state = 190
                self.expression(0)
                self.state = 191
                self.match(cpp_tinyParser.T__9)
                pass

            elif la_ == 3:
                self.state = 193
                self.variableName()
                pass

            elif la_ == 4:
                self.state = 194
                self.call()
                pass

            elif la_ == 5:
                self.state = 195
                self.typevalue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 227
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 198
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 199
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 200
                        self.expression(15)
                        pass

                    elif la_ == 2:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 201
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 202
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 203
                        self.expression(14)
                        pass

                    elif la_ == 3:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 204
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 205
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829140) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 206
                        self.expression(13)
                        pass

                    elif la_ == 4:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 207
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 208
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 209
                        self.expression(12)
                        pass

                    elif la_ == 5:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 210
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 211
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==29):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 212
                        self.expression(11)
                        pass

                    elif la_ == 6:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 213
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 214
                        _la = self._input.LA(1)
                        if not(_la==30 or _la==31):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 215
                        self.expression(10)
                        pass

                    elif la_ == 7:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 216
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 217
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 218
                        self.expression(9)
                        pass

                    elif la_ == 8:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 219
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 220
                        self.match(cpp_tinyParser.T__33)
                        self.state = 221
                        self.expression(0)
                        self.state = 222
                        self.match(cpp_tinyParser.T__17)
                        self.state = 223
                        self.expression(8)
                        pass

                    elif la_ == 9:
                        localctx = cpp_tinyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 225
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 226
                        _la = self._input.LA(1)
                        if not(_la==35 or _la==36):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
            self.state = 232
            self.match(cpp_tinyParser.T__12)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 142003816514978208) != 0):
                self.state = 233
                self.statement()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 239
            self.match(cpp_tinyParser.T__13)
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


        def expression(self):
            return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,0)


        def call(self):
            return self.getTypedRuleContext(cpp_tinyParser.CallContext,0)


        def condition(self):
            return self.getTypedRuleContext(cpp_tinyParser.ConditionContext,0)


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


        def forInit(self):
            return self.getTypedRuleContext(cpp_tinyParser.ForInitContext,0)


        def forIter(self):
            return self.getTypedRuleContext(cpp_tinyParser.ForIterContext,0)


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
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.definition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 243
                self.assignment()
                self.state = 244
                self.match(cpp_tinyParser.T__5)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.expression(0)
                self.state = 247
                self.match(cpp_tinyParser.T__5)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 249
                self.call()
                self.state = 250
                self.match(cpp_tinyParser.T__5)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 252
                self.match(cpp_tinyParser.T__36)
                self.state = 253
                self.match(cpp_tinyParser.T__6)
                self.state = 254
                self.condition()
                self.state = 255
                self.match(cpp_tinyParser.T__9)
                self.state = 258
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5, 7, 8, 21, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56]:
                    self.state = 256
                    self.statement()
                    pass
                elif token in [13]:
                    self.state = 257
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 265
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 260
                    self.match(cpp_tinyParser.T__37)
                    self.state = 263
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [5, 7, 8, 21, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56]:
                        self.state = 261
                        self.statement()
                        pass
                    elif token in [13]:
                        self.state = 262
                        self.block()
                        pass
                    else:
                        raise NoViableAltException(self)



                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 267
                self.match(cpp_tinyParser.T__38)
                self.state = 268
                self.match(cpp_tinyParser.T__6)
                self.state = 269
                self.condition()
                self.state = 270
                self.match(cpp_tinyParser.T__9)
                self.state = 273
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5, 7, 8, 21, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56]:
                    self.state = 271
                    self.statement()
                    pass
                elif token in [13]:
                    self.state = 272
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 275
                self.match(cpp_tinyParser.T__39)
                self.state = 276
                self.match(cpp_tinyParser.T__6)
                self.state = 277
                self.forInit()
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 141863491343483264) != 0):
                    self.state = 278
                    self.condition()


                self.state = 281
                self.match(cpp_tinyParser.T__5)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 141863491343483264) != 0):
                    self.state = 282
                    self.forIter()


                self.state = 285
                self.match(cpp_tinyParser.T__9)
                self.state = 288
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5, 7, 8, 21, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56]:
                    self.state = 286
                    self.statement()
                    pass
                elif token in [13]:
                    self.state = 287
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 290
                self.match(cpp_tinyParser.T__40)
                self.state = 291
                self.expression(0)
                self.state = 292
                self.match(cpp_tinyParser.T__5)
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
            self.state = 296
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
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 298
                self.declarationVariable()
                pass

            elif la_ == 2:
                self.state = 299
                self.definitionVariable()
                pass

            elif la_ == 3:
                self.state = 300
                self.statement()
                pass

            elif la_ == 4:
                self.state = 301
                self.match(cpp_tinyParser.T__5)
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
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
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
            self.state = 308
            self.variableName()
            self.state = 309
            self.match(cpp_tinyParser.T__10)
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 310
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 311
                self.arrayValue()
                pass

            elif la_ == 3:
                self.state = 312
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

        def variableName(self):
            return self.getTypedRuleContext(cpp_tinyParser.VariableNameContext,0)


        def NAME(self):
            return self.getToken(cpp_tinyParser.NAME, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,i)


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
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 315
                self.variableName()
                pass

            elif la_ == 2:
                self.state = 316
                self.match(cpp_tinyParser.NAME)
                pass


            self.state = 319
            self.match(cpp_tinyParser.T__6)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 141863491343483264) != 0):
                self.state = 320
                self.expression(0)
                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 321
                    self.match(cpp_tinyParser.T__8)
                    self.state = 322
                    self.expression(0)
                    self.state = 327
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 330
            self.match(cpp_tinyParser.T__9)
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
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.simpleType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
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
            self.state = 336
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2388139255529472) != 0)):
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
            self.state = 338
            self.simpleType()
            self.state = 339
            self.match(cpp_tinyParser.T__46)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 141863491343483264) != 0):
                self.state = 340
                self.expression(0)


            self.state = 343
            self.match(cpp_tinyParser.T__47)
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
            self.state = 345
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 139611588448485376) != 0)):
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


        def parentName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ParentNameContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ParentNameContext,i)


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
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 347
                self.nameSpace()
                self.state = 348
                self.match(cpp_tinyParser.T__48)


            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 352
                    self.parentName()
                    self.state = 353
                    self.match(cpp_tinyParser.T__2) 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8 or _la==21:
                self.state = 360
                _la = self._input.LA(1)
                if not(_la==8 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 363
                self.simpleVariable()
                pass

            elif la_ == 2:
                self.state = 364
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
            self.state = 367
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
            self.state = 369
            self.match(cpp_tinyParser.NAME)
            self.state = 375 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 370
                    self.match(cpp_tinyParser.T__46)
                    self.state = 372
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 141863491343483264) != 0):
                        self.state = 371
                        self.expression(0)


                    self.state = 374
                    self.match(cpp_tinyParser.T__47)

                else:
                    raise NoViableAltException(self)
                self.state = 377 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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

        def arrayValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ArrayValueContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ArrayValueContext,i)


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
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(cpp_tinyParser.T__12)
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 141863491343491456) != 0):
                    self.state = 380
                    self.arrayValue()
                    self.state = 385
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==9:
                        self.state = 381
                        self.match(cpp_tinyParser.T__8)
                        self.state = 382
                        self.arrayValue()
                        self.state = 387
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 390
                self.match(cpp_tinyParser.T__13)
                pass
            elif token in [7, 8, 21, 35, 36, 51, 52, 53, 54, 55, 56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
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

        def type_(self):
            return self.getTypedRuleContext(cpp_tinyParser.TypeContext,0)


        def expression(self):
            return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,0)


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
            self.state = 394
            self.match(cpp_tinyParser.T__49)
            self.state = 395
            self.type_()
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 396
                self.match(cpp_tinyParser.T__46)
                self.state = 397
                self.expression(0)
                self.state = 398
                self.match(cpp_tinyParser.T__47)


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


        def parentName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ParentNameContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ParentNameContext,i)


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
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 402
                self.nameSpace()
                self.state = 403
                self.match(cpp_tinyParser.T__48)


            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 407
                    self.parentName()
                    self.state = 408
                    self.match(cpp_tinyParser.T__2) 
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

            self.state = 415
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp_tinyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp_tinyParser.ExpressionContext,i)


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
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.simpleVariable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.arrayVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 419
                self.match(cpp_tinyParser.NAME)
                self.state = 432
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 420
                    self.match(cpp_tinyParser.T__6)
                    self.state = 429
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 141863491343483264) != 0):
                        self.state = 421
                        self.expression(0)
                        self.state = 426
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==9:
                            self.state = 422
                            self.match(cpp_tinyParser.T__8)
                            self.state = 423
                            self.expression(0)
                            self.state = 428
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)



                    self.state = 431
                    self.match(cpp_tinyParser.T__9)


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
            self.state = 436
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
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         




