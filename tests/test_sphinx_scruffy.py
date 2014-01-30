"""Tests for sphinx_scruffy."""
import os
import tempfile

import sphinx

import pytest

import sphinx_scruffy

BASE_DIR = os.path.dirname(__file__)


@pytest.fixture
def build_dir():
    """Test build dir for the sphinx compiled docs."""
    return tempfile.mkdtemp()


def test_sphinx_scruffy(build_dir):
    """Test sphinx_scruffy plugin."""
    res = sphinx.main(['-c ' + os.path.join(BASE_DIR, 'conf.py'), BASE_DIR, build_dir])
    assert res is 0
    assert 'index.html' in os.listdir(build_dir)


def test_sphinx_scruffy_error(monkeypatch, build_dir):
    """Test sphinx_scruffy plugin if renderer fails. Should not affect the whole build."""
    monkeypatch.setattr(sphinx_scruffy, 'render_scruffy', lambda *args, **kwargs: 1 / 0)
    res = sphinx.main(['-c ' + os.path.join(BASE_DIR, 'conf.py'), BASE_DIR, build_dir])
    assert res is 0
    assert 'index.html' in os.listdir(build_dir)
