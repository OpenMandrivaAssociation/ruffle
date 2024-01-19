Name:           ruffle
Version:        20240119
Release:        1
Summary:        Adobe Flash Player emulator written in Rust
License:        Apache-2.0 OR MIT
URL:            https://ruffle.rs/
Source0:         https://github.com/ruffle-rs/ruffle/archive/refs/tags/nightly-2024-01-19.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  cargo
BuildRequires:  rust-packaging
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(x11)

%description
Ruffle is an Adobe Flash Player emulator written in the Rust programming
language. Ruffle targets both the desktop and the web using WebAssembly.

%prep
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config


%build
%cargo_build

%install
#RUSTFLAGS=%%{rustflags} cargo install --root=%%{buildroot}%%{_prefix} --path .
# find out why this doesn't work
#%%cargo_install

install -Dm0755 target/release/ruffle_desktop %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
