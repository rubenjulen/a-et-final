import { registerRoot, Composition } from 'remotion';
import React from 'react';
import { KaderC } from './KaderC';
import tC from './timing_kC.json';

const FPS = 30;
const Root = () => (
  <Composition id="KaderC" component={KaderC} durationInFrames={Math.ceil(tC.total * FPS)} fps={FPS} width={1920} height={1080} />
);
registerRoot(Root);
