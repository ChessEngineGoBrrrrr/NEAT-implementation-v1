import pandas as pd
from stockfish import Stockfish
import chess
import random
board = chess.Board()
#number of positions 12672 so far




stockfish = Stockfish(path="C:/Users/user/Stockfish/stockfish/stockfish-windows-x86-64-avx2.exe", depth = 18)
pd.set_option("display.max_columns", 10000)
df = pd.read_csv("C:/Users/user/Downloads/200k_blitz_rapid_classical_bullet.csv")
df = df.fillna("NA")
print(df.loc[:, ["Move_ply_1", "Move_ply_2", "Move_ply_3", "Move_ply_4", "Move_ply_5", "Move_ply_6", "Move_ply_7", "Move_ply_8", "Move_ply_9", "Move_ply_10", "Move_ply_11", "Move_ply_12", "Move_ply_13", "Move_ply_14", "Move_ply_15", "Move_ply_16", "Move_ply_17", "Move_ply_18", "Move_ply_19", "Move_ply_20", "Move_ply_21", "Move_ply_22", "Move_ply_23", "Move_ply_24", "Move_ply_25", "Move_ply_26", "Move_ply_27", "Move_ply_28", "Move_ply_29", "Move_ply_30", "Move_ply_31", "Move_ply_32", "Move_ply_33", "Move_ply_34", "Move_ply_35", "Move_ply_36", "Move_ply_37", "Move_ply_38", "Move_ply_39", "Move_ply_40", "Move_ply_41", "Move_ply_42", "Move_ply_43", "Move_ply_44", "Move_ply_45", "Move_ply_46", "Move_ply_47", "Move_ply_48", "Move_ply_49", "Move_ply_50", "Move_ply_51", "Move_ply_52", "Move_ply_53", "Move_ply_54", "Move_ply_55", "Move_ply_56", "Move_ply_57", "Move_ply_58", "Move_ply_59", "Move_ply_60", "Move_ply_61", "Move_ply_62", "Move_ply_63", "Move_ply_64", "Move_ply_65", "Move_ply_66", "Move_ply_67", "Move_ply_68", "Move_ply_69", "Move_ply_70", "Move_ply_71", "Move_ply_72", "Move_ply_73", "Move_ply_74", "Move_ply_75", "Move_ply_76", "Move_ply_77", "Move_ply_78", "Move_ply_79", "Move_ply_80", "Move_ply_81", "Move_ply_82", "Move_ply_83", "Move_ply_84", "Move_ply_85", "Move_ply_86", "Move_ply_87", "Move_ply_88", "Move_ply_89", "Move_ply_90", "Move_ply_91", "Move_ply_92", "Move_ply_93", "Move_ply_94", "Move_ply_95", "Move_ply_96", "Move_ply_97", "Move_ply_98", "Move_ply_99", "Move_ply_100", "Move_ply_101", "Move_ply_102", "Move_ply_103", "Move_ply_104", "Move_ply_105", "Move_ply_106", "Move_ply_107", "Move_ply_108", "Move_ply_109", "Move_ply_110", "Move_ply_111", "Move_ply_112", "Move_ply_113", "Move_ply_114", "Move_ply_115", "Move_ply_116", "Move_ply_117", "Move_ply_118", "Move_ply_119", "Move_ply_120", "Move_ply_121", "Move_ply_122", "Move_ply_123", "Move_ply_124", "Move_ply_125", "Move_ply_126", "Move_ply_127", "Move_ply_128", "Move_ply_129", "Move_ply_130", "Move_ply_131", "Move_ply_132", "Move_ply_133", "Move_ply_134", "Move_ply_135", "Move_ply_136", "Move_ply_137", "Move_ply_138", "Move_ply_139", "Move_ply_140", "Move_ply_141", "Move_ply_142", "Move_ply_143", "Move_ply_144", "Move_ply_145", "Move_ply_146", "Move_ply_147", "Move_ply_148", "Move_ply_149", "Move_ply_150", "Move_ply_151", "Move_ply_152", "Move_ply_153", "Move_ply_154", "Move_ply_155", "Move_ply_156", "Move_ply_157", "Move_ply_158", "Move_ply_159", "Move_ply_160", "Move_ply_161", "Move_ply_162", "Move_ply_163", "Move_ply_164", "Move_ply_165", "Move_ply_166", "Move_ply_167", "Move_ply_168", "Move_ply_169", "Move_ply_170", "Move_ply_171", "Move_ply_172", "Move_ply_173", "Move_ply_174", "Move_ply_175", "Move_ply_176", "Move_ply_177", "Move_ply_178", "Move_ply_179", "Move_ply_180", "Move_ply_181", "Move_ply_182", "Move_ply_183", "Move_ply_184", "Move_ply_185", "Move_ply_186", "Move_ply_187", "Move_ply_188", "Move_ply_189", "Move_ply_190", "Move_ply_191", "Move_ply_192", "Move_ply_193", "Move_ply_194", "Move_ply_195", "Move_ply_196", "Move_ply_197", "Move_ply_198", "Move_ply_199", "Move_ply_200" ]])
coulumns = ["Move_ply_1", "Move_ply_2", "Move_ply_3", "Move_ply_4", "Move_ply_5", "Move_ply_6", "Move_ply_7", "Move_ply_8", "Move_ply_9", "Move_ply_10", "Move_ply_11", "Move_ply_12", "Move_ply_13", "Move_ply_14", "Move_ply_15", "Move_ply_16", "Move_ply_17", "Move_ply_18", "Move_ply_19", "Move_ply_20", "Move_ply_21", "Move_ply_22", "Move_ply_23", "Move_ply_24", "Move_ply_25", "Move_ply_26", "Move_ply_27", "Move_ply_28", "Move_ply_29", "Move_ply_30", "Move_ply_31", "Move_ply_32", "Move_ply_33", "Move_ply_34", "Move_ply_35", "Move_ply_36", "Move_ply_37", "Move_ply_38", "Move_ply_39", "Move_ply_40", "Move_ply_41", "Move_ply_42", "Move_ply_43", "Move_ply_44", "Move_ply_45", "Move_ply_46", "Move_ply_47", "Move_ply_48", "Move_ply_49", "Move_ply_50", "Move_ply_51", "Move_ply_52", "Move_ply_53", "Move_ply_54", "Move_ply_55", "Move_ply_56", "Move_ply_57", "Move_ply_58", "Move_ply_59", "Move_ply_60", "Move_ply_61", "Move_ply_62", "Move_ply_63", "Move_ply_64", "Move_ply_65", "Move_ply_66", "Move_ply_67", "Move_ply_68", "Move_ply_69", "Move_ply_70", "Move_ply_71", "Move_ply_72", "Move_ply_73", "Move_ply_74", "Move_ply_75", "Move_ply_76", "Move_ply_77", "Move_ply_78", "Move_ply_79", "Move_ply_80", "Move_ply_81", "Move_ply_82", "Move_ply_83", "Move_ply_84", "Move_ply_85", "Move_ply_86", "Move_ply_87", "Move_ply_88", "Move_ply_89", "Move_ply_90", "Move_ply_91", "Move_ply_92", "Move_ply_93", "Move_ply_94", "Move_ply_95", "Move_ply_96", "Move_ply_97", "Move_ply_98", "Move_ply_99", "Move_ply_100", "Move_ply_101", "Move_ply_102", "Move_ply_103", "Move_ply_104", "Move_ply_105", "Move_ply_106", "Move_ply_107", "Move_ply_108", "Move_ply_109", "Move_ply_110", "Move_ply_111", "Move_ply_112", "Move_ply_113", "Move_ply_114", "Move_ply_115", "Move_ply_116", "Move_ply_117", "Move_ply_118", "Move_ply_119", "Move_ply_120", "Move_ply_121", "Move_ply_122", "Move_ply_123", "Move_ply_124", "Move_ply_125", "Move_ply_126", "Move_ply_127", "Move_ply_128", "Move_ply_129", "Move_ply_130", "Move_ply_131", "Move_ply_132", "Move_ply_133", "Move_ply_134", "Move_ply_135", "Move_ply_136", "Move_ply_137", "Move_ply_138", "Move_ply_139", "Move_ply_140", "Move_ply_141", "Move_ply_142", "Move_ply_143", "Move_ply_144", "Move_ply_145", "Move_ply_146", "Move_ply_147", "Move_ply_148", "Move_ply_149", "Move_ply_150", "Move_ply_151", "Move_ply_152", "Move_ply_153", "Move_ply_154", "Move_ply_155", "Move_ply_156", "Move_ply_157", "Move_ply_158", "Move_ply_159", "Move_ply_160", "Move_ply_161", "Move_ply_162", "Move_ply_163", "Move_ply_164", "Move_ply_165", "Move_ply_166", "Move_ply_167", "Move_ply_168", "Move_ply_169", "Move_ply_170", "Move_ply_171", "Move_ply_172", "Move_ply_173", "Move_ply_174", "Move_ply_175", "Move_ply_176", "Move_ply_177", "Move_ply_178", "Move_ply_179", "Move_ply_180", "Move_ply_181", "Move_ply_182", "Move_ply_183", "Move_ply_184", "Move_ply_185", "Move_ply_186", "Move_ply_187", "Move_ply_188", "Move_ply_189", "Move_ply_190", "Move_ply_191", "Move_ply_192", "Move_ply_193", "Move_ply_194", "Move_ply_195", "Move_ply_196", "Move_ply_197", "Move_ply_198", "Move_ply_199", "Move_ply_200" ]
Position_List = []
print(stockfish.get_parameters())
for j in range(1000):
	for i in range(200):
		Current_Move = df.loc[j + 2000, coulumns[i]]
		if Current_Move == "NA":
			break
		board.push_san(Current_Move)
		if random.randint(1,10) < 2:
			stockfish.set_fen_position(board.fen())
			Position_List.append([stockfish.get_evaluation(), board.fen()])
	board.reset()
print(Position_List)
