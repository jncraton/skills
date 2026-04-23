use pyo3::prelude::*;

#[pyfunction]
fn hello(name: Option<&str>) -> String {
  let who = name.unwrap_or("world");
  format!("Hello, {}!", who)
}

#[pymodule]
fn pyo3_example(m: &Bound<'_, PyModule>) -> PyResult<()> {
  m.add_function(wrap_pyfunction!(hello, m)?)?;
  Ok(())
}