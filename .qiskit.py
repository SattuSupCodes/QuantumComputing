import os
from setuptools import setup # type: ignore
from setuptools_rust import Binding, RustExtension # type: ignore

setup(
    rust_extensions=[
        RustExtension(
            "qiskit._accelerate",
            "crates/pyext/Cargo.toml",
            binding=Binding.PyO3,
            debug=rust_debug, # type: ignore
            features=features, # type: ignore
        )
    ],
    options={"bdist_wheel": {"py_limited_api": "cp38"}},
)