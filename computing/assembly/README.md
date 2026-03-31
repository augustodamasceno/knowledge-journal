# Assembly  

## x86/x64 Architecture

### Essential References

* **Intel 64 and IA-32 Architectures Software Developer's Manual** (Intel Corporation, 2023+) - Ground truth for every instruction. Non-negotiable reference.
* **Agner Fog optimization manuals** - Best practical optimization resource. Microarch tables, SIMD, pipelines. Available: https://agner.org/optimize
* **AMD64 ABI** - Calling conventions, register usage, stack layout. Available: https://refspecs.linuxfoundation.org

### Books

* R. E. Bryant and D. R. O'Hallaron, *Computer Systems: A Programmer's Perspective*, 3rd ed. Boston, MA: Pearson, 2016. - Best structured book for x86-64 + systems together.
* D. Kusswurm, *Modern X86 Assembly Language Programming*, 3rd ed. New York: Apress, 2023. - Covers SSE/AVX/AVX-512 explicitly, C++ integration.
* R. Hyde, *The Art of 64-Bit Assembly Language*, San Francisco: No Starch Press, 2021. - Extremely detailed, MASM-based but concepts transfer.

### Tools & Analysis

* **uops.info** - Per-instruction latency/throughput tables for Intel/AMD
* **LLVM MCA** (via Compiler Explorer) - Simulates pipeline execution of assembly
* **Compiler Explorer** (godbolt.org) - Read compiler output live

## ARM/AArch64 Architecture

### Essential References

* **ARM Architecture Reference Manual (ARM ARM)** - The SDM equivalent for ARM. Available: https://developer.arm.com
* **ARM Cortex-A Programmer's Guide** - More readable than ARM ARM, practical focus.
* **NEON Programmer's Guide** - Dedicated SIMD for ARM, covers intrinsics and assembly.

### Books

* J. Yiu, *The Definitive Guide to ARM Cortex-M3 and Cortex-M4 Processors*, 3rd ed. Oxford: Newnes, 2013.
* S. Warford, *Programming with 64-Bit ARM Assembly Language*, New York: Apress, 2020. - Modern AArch64, Raspberry Pi focused, practical.
* W. Pyeatt and W. Ughetta, *ARM 64-Bit Assembly Language*, New York: Newnes, 2019. - More rigorous, covers NEON SIMD.

## RISC-V Architecture

* D. Patterson and A. Waterman, *The RISC-V Reader: An Open Architecture Atlas*, 1st ed. Berkeley, CA: Strawberry Canyon, 2017.
* D. A. Patterson and J. L. Hennessy, *Computer Organization and Design: The Hardware/Software Interface*, RISC-V Edition. Cambridge, MA: Morgan Kaufmann, 2017.

## Cross-Architecture & Performance

### Books & Guides

* D. Bakhvalov, *Performance Analysis and Tuning on Modern CPUs*. Free online book covering x86+ARM, perf tools, microarchitecture. Available: https://book.easyperf.net
* **Brendan Gregg's work** - Perf, flamegraphs, Linux profiling. Available: https://brendangregg.com

### Books & Guides

* D. Bakhvalov, *Performance Analysis and Tuning on Modern CPUs*. Free online book covering x86+ARM, perf tools, microarchitecture. Available: https://book.easyperf.net
* **Brendan Gregg's work** - Perf, flamegraphs, Linux profiling. Available: https://brendangregg.com

### Performance Analysis Tools

```bash
perf + perf annotate       # See hot assembly in real workloads
objdump / llvm-objdump     # Disassemble real binaries
Intel VTune / AMD uProf    # Microarchitecture profiling
```

## Recommended Learning Path

1. **CS:APP** (Bryant & O'Hallaron) → Solidify x86-64 mental model
2. **Agner Fog manuals** → Optimization + SIMD practice
3. **Kusswurm** (Modern X86) → AVX/AVX-512 deep dive
4. **ARM ARM + NEON guide** → AArch64 + SIMD
5. **Bakhvalov** → Cross-arch performance tuning
6. **Intel SDM / ARM ARM** → Permanent reference shelf
