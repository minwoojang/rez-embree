name = "embree"

version = "3.2.2"

description = """
    Intel® Embree is a collection of high-performance ray tracing kernels, developed at Intel. The target users
    of Intel® Embree are graphics application engineers who want to improve the performance of their photo-realistic
    rendering application by leveraging Embree's performance-optimized ray tracing kernels.
    """

authors = [
    "Intel",
]

requires = [
    "cmake-3",
]

variants = [['platform-linux', 'arch-x86_64']]

build_system = "cmake"


with scope("config") as config:
    config.build_thread_count = "logical_cores"


def commands():
    env.LIBRARY_PATH.prepend("{root}/lib")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.CPATH.prepend("{root}/include")
    env.embree_DIR.set("{root}")
    env.CMAKE_MODULE_PATH.prepend("{root}/lib/cmake/embree-{version}")

    # Helper environment variables.
    env.EMBREE_BINARY_PATH.set("{root}/bin")
    env.EMBREE_INCLUDE_PATH.set("{root}/include")
    env.EMBREE_LIBRARY_PATH.set("{root}/lib")
