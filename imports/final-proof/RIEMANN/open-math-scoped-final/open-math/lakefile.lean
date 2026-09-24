import Lake
open Lake DSL

package open_math_minimal where

require «m-core-riemann» from git
  "https://github.com/ShantiDraconis/m-core-riemann.git" @
  "5c66f8dca03834f24a61a9b1219e7af9d4892dd6"

@[default_target]
lean_lib Riemann where
