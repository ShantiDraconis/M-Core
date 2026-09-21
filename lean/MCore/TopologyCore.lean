import Mathlib

namespace MCore.Topology

def IsClosedR (s : Set ℝ) : Prop := _root_.IsClosed s
def interiorR (s : Set ℝ) : Set ℝ := _root_.interior s
def closureR (s : Set ℝ) : Set ℝ := _root_.closure s
def frontierR (s : Set ℝ) : Set ℝ := _root_.frontier s

end MCore.Topology
