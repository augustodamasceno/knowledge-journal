# C++

## 1.1 [Notes for **Effective Modern C++** [Reference 5]](effective-modern-cpp.md)

## 1.2 SIMD / AVX register quick reference

| Register group | Width | HW names | C++ type names (intrinsics) | Common intrinsic functions in C++ | Description |
|---|---:|---|---|---|---|
| MMX | 64-bit | `mm0`-`mm7` | `__m64` | `_mm_set_pi16`, `_mm_add_pi16`, `_mm_sub_pi16`, `_mm_mulhi_pi16`, `_mm_unpackhi_pi16`, `_mm_empty` | Legacy packed-integer SIMD registers (alias x87 FP state); mostly obsolete in new code. |
| XMM | 128-bit | `xmm0`-`xmm31` | `__m128`, `__m128d`, `__m128i` | `_mm_set1_ps`, `_mm_loadu_ps`, `_mm_add_ps`, `_mm_mul_ps`, `_mm_and_ps`, `_mm_cmplt_ps`, `_mm_shuffle_ps`, `_mm_storeu_ps` | SSE/SSE2+ vectors; also low 128 bits of YMM/ZMM. |
| YMM | 256-bit | `ymm0`-`ymm31` | `__m256`, `__m256d`, `__m256i` | `_mm256_set1_ps`, `_mm256_loadu_ps`, `_mm256_add_ps`, `_mm256_mul_ps`, `_mm256_fmadd_ps`, `_mm256_blend_ps`, `_mm256_permutevar8x32_ps`, `_mm256_storeu_ps` | AVX/AVX2 vectors; extend XMM to 256 bits. |
| ZMM | 512-bit | `zmm0`-`zmm31` | `__m512`, `__m512d`, `__m512i` | `_mm512_set1_ps`, `_mm512_loadu_ps`, `_mm512_add_ps`, `_mm512_mul_ps`, `_mm512_fmadd_ps`, `_mm512_permutexvar_ps`, `_mm512_reduce_add_ps`, `_mm512_storeu_ps` | AVX-512 vectors; extend YMM/XMM to 512 bits. |
| Opmask (`k`) | 8/16/32/64-bit masks | `k0`-`k7` | `__mmask8`, `__mmask16`, `__mmask32`, `__mmask64` | `_mm512_cmp_ps_mask`, `_mm512_kand`, `_mm512_kor`, `_mm512_kxor`, `_mm512_mask_add_ps`, `_mm512_maskz_add_ps` | AVX-512 lane masks controlling merge/zero behavior. |
| Tile (`tmm`) | 2D tile state | `tmm0`-`tmm7` | (configured through AMX tile APIs) | `_tile_loadconfig`, `_tile_loadd`, `_tile_stream_loadd`, `_tile_dpbf16ps`, `_tile_dpbssd`, `_tile_dpbsud`, `_tile_stored`, `_tile_release` | AMX matrix tiles; separate ISA from AVX but part of SIMD evolution. |

Notes:
- `xmmN`, `ymmN`, and `zmmN` are overlapping views of the same logical vector register number `N`.
- Wider AVX-512 register files (`xmm16`-`xmm31`, `ymm16`-`ymm31`, `zmm16`-`zmm31`) require AVX-512 support.
- In common C/C++ intrinsics headers, types usually map as: `__m128` -> XMM, `__m256` -> YMM, `__m512` -> ZMM.
- In normal C++ you use intrinsic types/functions; you usually do not pick exact register numbers (`xmm3`, `ymm7`, etc.), because the compiler register allocator chooses them.

## 1.3 References  

* [1] "C++ Standard Library headers," cppreference.com. [Online]. Available: https://en.cppreference.com/w/cpp/header.html. [Accessed: Dec. 24, 2025].
* [2] B. Stroustrup, *The C++ Programming Language*, 4th ed. Boston, MA, USA: Addison-Wesley, 2013.  
* [3] B. Stroustrup, *A Tour of C++*, 3rd ed. Boston, MA, USA: Addison-Wesley, 2022.
* [4] M. Gregoire, *Professional C++*, 6th ed. Hoboken, NJ, USA: Wiley, 2024.  
* [5] S. Meyers, *Effective Modern C++*. Sebastopol, CA, USA: O'Reilly Media, 2015.  
* [6] S. Meyers, *Effective C++*, 3rd ed. Boston, MA, USA: Addison-Wesley, 2005.
* [7] S. Meyers, *More Effective C++*. Boston, MA, USA: Addison-Wesley, 1996.
* [8] S. Ghosh, *Building Low Latency Applications with C++*. Birmingham, UK: Packt Publishing, 2023.  
* [9] N. M. Josuttis, *C++ Templates: The Complete Guide*, 2nd ed. Boston, MA, USA: Addison-Wesley, 2017.  
* [10] A. Williams, *C++ Concurrency in Action*, 2nd ed. Shelter Island, NY, USA: Manning Publications, 2019.  
* [11] K. Guntheroth, *Optimized C++*. Sebastopol, CA, USA: O'Reilly Media, 2016.  
* [12] J. Lakos, V. Romeo, R. Khlebnikov, and A. Meredith, *Embracing Modern C++ Safely*. Boston, MA, USA: Addison-Wesley, 2021.  
* [13] N. M. Josuttis, *The C++ Standard Library*, 2nd ed. Boston, MA, USA: Addison-Wesley, 2012.
* [14] I. Horton and P. Van Weert, *Beginning C++20: From Novice to Professional*, 6th ed. Berkeley, CA, USA: Apress, 2020.
* [15] N. M. Josuttis, *C++20 - The Complete Guide*. Nicojosuttis, 2022.
* [16] M. Cukic, *Functional Programming in C++*. Shelter Island, NY, USA: Manning Publications, 2018.
* [17] K. Iglberger, *C++ Software Design*. Sebastopol, CA, USA: O'Reilly Media, 2022.
* [18] F. G. Pikus, *The Art of Writing Efficient Programs*. Birmingham, UK: Packt Publishing, 2021.
* [19] D. Duffy, *Financial Instrument Pricing Using C++*, 2nd ed. Hoboken, NJ, USA: Wiley, 2018.
* [20] D. J. Duffy, *Introduction to C++ for Financial Engineers*. Hoboken, NJ, USA: Wiley, 2017.
* [21] J. London, *Modeling Derivatives in C++*. Hoboken, NJ, USA: Wiley, 2004.
* [22] C. Scott, *Professional CMake: A Practical Guide*, 1st ed. Crascit Pty Ltd, 2018.
* [23] "ISO/IEC 14882:2020 Programming languages — C++," International Organization for Standardization, 2020.
* [24] "CMake Documentation," Kitware. [Online]. Available: https://cmake.org/documentation/. [Accessed: Dec. 24, 2025].
* [25] "C++ Core Guidelines," Standard C++ Foundation. [Online]. Available: https://isocpp.github.io/CppCoreGuidelines/. [Accessed: Dec. 24, 2025].
* [26] N. M. Josuttis, *C++23 - The Complete Guide*. Leanpub, 2023.
* [27] H. Sutter, *Exceptional C++: 47 Engineering Puzzles, Programming Problems, and Solutions*. Boston, MA, USA: Addison-Wesley, 2000.
* [28] H. Sutter and A. Alexandrescu, *C++ Coding Standards: 101 Rules, Guidelines, and Best Practices*. Boston, MA, USA: Addison-Wesley, 2005.
* [29] "Conan Documentation," Conan.io. [Online]. Available: https://docs.conan.io/. [Accessed: Dec. 24, 2025].
* [30] "vcpkg Documentation," Microsoft. [Online]. Available: https://vcpkg.io/. [Accessed: Dec. 24, 2025].
* [31] J. Langr, *Modern C++ Programming with Test-Driven Development: Code Better, Sleep Better*. Dallas, TX, USA: Pragmatic Bookshelf, 2013.
* [32] J. Boccara, "Fluent C++," Fluent C++. [Online]. Available: https://www.fluentcpp.com/. [Accessed: Feb. 17, 2026].
* [33] "Compiler Explorer," Godbolt. [Online]. Available: https://godbolt.org/. [Accessed: Feb. 17, 2026].
* [34] "C++ Shell," cpp.sh. [Online]. Available: https://cpp.sh/. [Accessed: Feb. 17, 2026].
* [35] Intel, "Intel 64 and IA-32 Architectures Software Developer's Manual," vols. 1-4. [Online]. Available: https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. [Accessed: May 7, 2026].
* [36] Intel, "Intel Intrinsics Guide (searchable per-intrinsic index)." [Online]. Available: https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html. [Accessed: May 7, 2026].
* [37] AMD, "AMD64 Architecture Programmer's Manual, Volumes 1-5." [Online]. Available: https://www.amd.com/en/support/tech-docs/amd64-architecture-programmers-manual-volumes-1-5. [Accessed: May 7, 2026].
* [38] GCC, "x86 Built-in Functions (x86 intrinsics families/index)," GCC Online Documentation. [Online]. Available: https://gcc.gnu.org/onlinedocs/gcc/x86-Built-in-Functions.html. [Accessed: May 7, 2026].
* [39] Clang, "Language Extensions - x86/X86-64 Intrinsics and Builtins (index-style)," Clang documentation. [Online]. Available: https://clang.llvm.org/docs/LanguageExtensions.html. [Accessed: May 7, 2026].
* [40] Microsoft, "x86 intrinsics list (index-style)," Microsoft Learn. [Online]. Available: https://learn.microsoft.com/cpp/intrinsics/x86-intrinsics-list. [Accessed: May 7, 2026].
* [41] LLVM Project, "`avxintrin.h` (Clang AVX intrinsic declarations, including `_mm256_loadu_ps`)." [Online]. Available: https://github.com/llvm/llvm-project/blob/main/clang/lib/Headers/avxintrin.h. [Accessed: May 7, 2026].
* [42] Felix Cloutier, "x86 Instruction Reference: `MOVUPS/VMOVUPS` (instruction behind unaligned float loads)." [Online]. Available: https://www.felixcloutier.com/x86/movups. [Accessed: May 7, 2026].