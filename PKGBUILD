pkgname=CLATodoList
pkgver=0.3.1
pkgrel=1
pkgdesc="Simple CLA application for make todo"
arch=('any')
url="https://github.com/Lahanig/CLATodoList"
license=('MIT')
depends=('python>=3.13.7')
makedepends=('python-pipx')
source=("git+file://${startdir}")
#source=("$pkgname-$pkgver.tar.gz::https://github.com/Lahanig/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('SKIP')

build() {
    cd "$srcdir"
    
    pipx install pyinstaller

    python3 build_app.py
}

package() {
    cd "$srcdir/.."

    #install -Dm644 CLATodoList-icon.png "$HOME/.local/share/icons/CLATodoList-icon.png"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    #install -Dm644 CLATodoList.desktop "$HOME/.local/share/applications/CLATodoList.desktop"

    cd "$srcdir/dist"

    install -Dm755 $pkgname "$pkgdir/usr/bin/$pkgname"
}
