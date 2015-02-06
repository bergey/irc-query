{ pkgs ? import <nixpkgs> {} }:

# TODO distinguish between real build inputs and development tools
# (eg, ipython) For now, I'm not using Nix for deploy, so it works to
# list them all, and delete the dev tools when I generate
# requirements.txt
pkgs.stdenv.mkDerivation {
    name = "irc-query";
    version = "0.1";
    src = ./.;
    buildInputs = with pkgs.python33Packages; [
        pkgs.python33
        ipython
        flask
        sqlalchemy
        psycopg2
        pip
        gunicorn
    ];
}
