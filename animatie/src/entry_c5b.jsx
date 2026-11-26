import { registerRoot, Composition } from 'remotion';
import React from 'react';
import { Clip5b } from './Clip5b';
import t from './timing_c5b.json';

const FPS = 30;
const Root = () => (<>
  <Composition id="Clip5b" component={Clip5b} durationInFrames={Math.ceil(t.total * FPS)} fps={FPS} width={1920} height={1080} />
</>);
registerRoot(Root);
